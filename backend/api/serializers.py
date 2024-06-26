import base64

from django.core.files.base import ContentFile
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from recipe.models import Ingredient, IngredientAmount, Recipe, Tag, User
from .constants import MIN_VALUE, MAX_VALUE


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class UserCreateSerializer(UserCreateSerializer):
    def validate(self, attrs):
        return attrs


class UserGetSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'email', 'id', 'username', 'first_name',
            'last_name', 'is_subscribed')

    def get_is_subscribed(self, obj):
        request = self.context['request']
        if request.user.is_anonymous:
            return False
        return obj.subscriber.filter(user=request.user).exists()


class IngredientSerializer(serializers.ModelSerializer):
    amount = serializers.ReadOnlyField(source='recipes.amount')

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit', 'amount')


class IngredientAmountSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit')

    class Meta:
        model = IngredientAmount
        fields = ('id', 'name', 'measurement_unit', 'amount')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class RecipeGetSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    author = UserGetSerializer(read_only=True,)
    ingredients = IngredientAmountSerializer(read_only=True,
                                             many=True,
                                             source='ingredient_recipe')
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = (
            'id', 'tags', 'author', 'ingredients', 'is_favorited',
            'is_in_shopping_cart', 'name', 'image', 'text', 'cooking_time'
        )

    def get_is_favorited(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return user.is_favorited.filter(recipe=obj).exists()
        return False

    def get_is_in_shopping_cart(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return user.is_in_shopping_cart.filter(recipe=obj).exists()
        return False


class IngredientAmountCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='ingredient.id')
    amount = serializers.IntegerField(min_value=MIN_VALUE,
                                      max_value=MAX_VALUE)

    class Meta:
        model = IngredientAmount
        fields = ('id', 'amount')


class RecipeCreateSerializer(serializers.ModelSerializer):
    ingredients = IngredientAmountCreateSerializer(many=True,
                                                   source='ingredient_recipe',
                                                   required=True)
    tags = serializers.PrimaryKeyRelatedField(many=True,
                                              queryset=Tag.objects.all())
    image = Base64ImageField()
    cooking_time = serializers.IntegerField(min_value=MIN_VALUE,
                                            max_value=MAX_VALUE)

    class Meta:
        model = Recipe
        fields = ('ingredients', 'tags', 'name', 'image',
                  'text', 'cooking_time')
        read_only_fields = ('author',)

    def validate_tags(self, value):
        if not value:
            raise serializers.ValidationError('Отсутствуют теги')
        if len(value) != len(set(value)):
            raise serializers.ValidationError(
                'Теги должны быть уникальными'
            )
        return value

    def validate_ingredients(self, value):
        if not value:
            raise serializers.ValidationError('Отсутствуют ингредиенты')
        ingredient_list = set()
        for ingredient in value:
            ingredient_id = ingredient['ingredient']['id']
            if not Ingredient.objects.filter(id=ingredient_id).exists():
                raise serializers.ValidationError('Такого игредиента нет')
            if ingredient_id in ingredient_list:
                raise serializers.ValidationError(
                    'Ингредиенты должны быть уникальными'
                )
            ingredient_list.add(ingredient_id)
        return value

    def create_update_ingredients_amount(self, ingredient_recipe, recipe):
        ingrediens_amount = []
        for ingredient in ingredient_recipe:
            ingredient_id = ingredient['ingredient']['id']
            ingredient_amount = ingredient['amount']
            current_ingredient = Ingredient.objects.get(id=ingredient_id)
            ingrediens_amount.append(IngredientAmount(
                ingredient=current_ingredient,
                recipe=recipe,
                amount=ingredient_amount))
        IngredientAmount.objects.bulk_create(ingrediens_amount)

    def create(self, validated_data):
        ingredient_recipe = validated_data.pop('ingredient_recipe')
        tags = validated_data.pop('tags', None)

        recipe = Recipe.objects.create(**validated_data)
        recipe.tags.set(tags)

        self.create_update_ingredients_amount(
            ingredient_recipe=ingredient_recipe,
            recipe=recipe
        )
        return recipe

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.text = validated_data.get('text', instance.text)
        instance.cooking_time = validated_data.get(
            'cooking_time', instance.cooking_time
        )
        instance.image = validated_data.get('image', instance.image)

        tags = validated_data.pop('tags', [])
        if not tags:
            raise serializers.ValidationError(
                'Должен быть хотя бы один тег'
            )

        instance.tags.set(tags)

        ingredient_recipe = validated_data.pop('ingredient_recipe', [])
        if not ingredient_recipe:
            raise serializers.ValidationError(
                'Должен быть хотя бы один ингредиент'
            )
        instance.ingredient_recipe.all().delete()

        self.create_update_ingredients_amount(
            ingredient_recipe=ingredient_recipe,
            recipe=instance
        )
        instance.save()
        return instance

    def to_representation(self, instance):
        return RecipeGetSerializer(
            instance,
            context={'request': self.context.get('request')}
        ).data


class RecipeShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class SubscriptionsSerializer(UserGetSerializer):
    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'email', 'id', 'username', 'first_name',
            'last_name', 'is_subscribed', 'recipes',
            'recipes_count'
        )

    def get_recipes(self, obj):
        request = self.context['request']
        limit = request.query_params.get('recipes_limit')

        if request.user.is_anonymous:
            return False
        recipes = obj.recipes.all()
        if limit:
            recipes = recipes[:int(limit)]
        return RecipeShortSerializer(recipes, many=True).data

    def get_recipes_count(self, obj):
        return obj.recipes.all().count()
