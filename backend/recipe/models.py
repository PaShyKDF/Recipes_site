from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from api.constants import MIN_VALUE, MAX_VALUE

User = get_user_model()


class Tag(models.Model):
    name = models.CharField('Название тега', max_length=50)
    color = models.CharField('Цвет в 16-ом формате', max_length=16,
                             help_text='Пример шестнадцатеричного '
                             'кода цвета - #49B64E')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'Теги'
        ordering = ('slug',)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField('Название ингредиента', max_length=100,
                            db_index=True)
    measurement_unit = models.CharField('Единицы измерения',
                                        max_length=10)

    class Meta:
        verbose_name = 'ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField('Название рецепта', max_length=200, unique=True)
    image = models.ImageField('Фото', upload_to='recipes/images/')
    text = models.TextField('Описание')
    ingredients = models.ManyToManyField(Ingredient,
                                         through='IngredientAmount',
                                         verbose_name='Ингредиенты',
                                         related_name='ingredients')
    author = models.ForeignKey(User,
                               related_name='recipes',
                               on_delete=models.CASCADE,
                               verbose_name='Автор рецепта')
    tags = models.ManyToManyField(Tag,
                                  verbose_name='Теги рецепта',
                                  related_name='tags')
    cooking_time = models.PositiveSmallIntegerField(
        'Время приготовления в минутах',
        validators=[
            MinValueValidator(MIN_VALUE,
                              'минимальное время '
                              f'приготовления {MIN_VALUE} минута'
                              ),
            MaxValueValidator(MAX_VALUE,
                              'Максимальное время '
                              f'приготовления {MAX_VALUE} минута')
        ]
    )
    pub_date = models.DateTimeField(verbose_name='Дата и время публикации',
                                    auto_now_add=True)

    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date',)
        constraints = (
            models.UniqueConstraint(
                fields=['author', 'name'],
                name='unique_author_name'
            ),
        )

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient,
                                   verbose_name='Ингредиент',
                                   on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        validators=[
            MinValueValidator(MIN_VALUE, f'минимальное значение {MIN_VALUE}'),
            MaxValueValidator(MAX_VALUE, f'максимальное значение {MAX_VALUE}')
        ])

    class Meta:
        default_related_name = 'ingredient_recipe'
        verbose_name = 'ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('recipe',)
        constraints = (
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_recipe_ingredient'
            ),
        )

    def __str__(self):
        return self.recipe.name


class Favorited(models.Model):
    user = models.ForeignKey(User,
                             related_name='is_favorited',
                             verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe,
                               verbose_name='Рецепт',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'в избранных'
        verbose_name_plural = 'В избранных'
        ordering = ('user',)
        constraints = (
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_favorited_user_recipe'
            ),
        )


class ShoppingCart(models.Model):
    user = models.ForeignKey(User,
                             related_name='is_in_shopping_cart',
                             verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe,
                               verbose_name='Рецепт',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'в корзине'
        verbose_name_plural = 'В корзине'
        ordering = ('user',)
        constraints = (
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_shopping_cart_user_recipe'
            ),
        )

    def __str__(self):
        return f'{self.user} - {self.recipe}'
