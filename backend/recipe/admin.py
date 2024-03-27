from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Favorited, Ingredient, IngredientAmount, Recipe, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color',
        'slug',
    )


class IngredientAmountInline(admin.TabularInline):
    model = IngredientAmount
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'author',
        'cooking_time',
        'pub_date',
        'added_to_favorites_amount',
    )
    inlines = [IngredientAmountInline]
    list_filter = ['name', 'tags', 'author__username']

    def added_to_favorites_amount(self, obj):
        return Favorited.objects.filter(recipe=obj).count()

    added_to_favorites_amount.short_description = 'Добавлений в избранное'


class FavoritedAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'recipe',
    )


class IngredientResource(resources.ModelResource):
    class Meta:
        model = Ingredient


class IngredientAdmin(ImportExportModelAdmin):
    resource_class = IngredientResource
    list_display = (
        'name',
        'measurement_unit',
    )
    list_filter = ('name',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Favorited, FavoritedAdmin)
admin.site.register(Ingredient, IngredientAdmin)
