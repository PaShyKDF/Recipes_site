from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from .views import (
    IngredientViewSet,
    TagViewSet,
    RecipeViewSet,
    UserViewSet
)


app_name = 'api'


router = DefaultRouter()
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('users', UserViewSet)
router.register('tags', TagViewSet)
router.register('recipes', RecipeViewSet, basename='recipes')


urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
