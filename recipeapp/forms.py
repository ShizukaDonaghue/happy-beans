from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    """ Form used to post a comment """
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """
    Form used to post a recipe
    Summernote widget is used for Ingredients and Method fields
    """
    class Meta:
        model = Recipe
        fields = (
            'title',
            'description',
            'meal_type',
            'main_ingredient',
            'diet_type',
            'difficulty',
            'prep_time',
            'cook_time',
            'serves',
            'ingredients',
            'method',
            'image',
            'status',
        )
        widgets = {
            'ingredients': SummernoteWidget(),
            'method': SummernoteWidget(),
        }
