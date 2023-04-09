import django_filters
from .models import Recipe


class RecipeFilter(django_filters.FilterSet):
    """
    Recipe filters used in Browse Recipes page
    """

    class Meta:
        model = Recipe
        fields = ['meal_type', 'main_ingredient', 'difficulty']
