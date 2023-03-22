from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from cloudinary.models import CloudinaryField


class ChoiceArrayField(ArrayField):
    """
    This is a field that stores an array of choices.
    Uses Django's postgres ArrayField and a MultipleChoiceField for its
    formfield with a CheckboxSelectMultiple widget to create an array.
    Original codes from https://rogulski.it/django-multiselect-choice-admin/
    """
    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
            "widget": forms.CheckboxSelectMultiple,
            **kwargs
        }
        return super(ArrayField, self).formfield(**defaults)


# Status choices for the Recipe model
STATUS = (
    (0, 'Save as Draft'),
    (1, 'Publish Now!')
)


# Meal type choices for the Recipe model
MEAL_TYPE = (
    (0, 'Breakfast'),
    (1, 'Lunch'),
    (2, 'Dinner'),
    (3, 'Snack'),
    (4, 'Dessert'),
    (5, 'Drinks')
)


# Main ingredient choices for the Recipe model
MAIN_INGREDIENT = (
    (0, 'Beef'),
    (1, 'Chicken'),
    (2, 'Fruits'),
    (3, 'Grains'),
    (4, 'Lamb'),
    (5, 'Pork'),
    (6, 'Seafood'),
    (7, 'Turkey'),
    (8, 'Vegetable')
)


# Diet type multiple choices for the Recipe model
DIET_TYPES = (
    ('Dairy-free', 'Dairy-free'),
    ('Egg free', 'Egg free'),
    ('Gluten-free', 'Gluten-free'),
    ('Nut free', 'Nut free'),
    ('Vegan', 'Vegan'),
    ('Vegetarian', 'Vegetarian')
)

# Difficulty level choices for the Recipe model
DIFFICULTY = (
    (0, 'Easy'),
    (1, 'Moderate'),
    (2, 'Hard')
)


class Recipe(models.Model):
    """ Model for recipes """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipe_posts'
    )
    description = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    meal_type = models.IntegerField(choices=MEAL_TYPE)
    main_ingredient = models.IntegerField(choices=MAIN_INGREDIENT)
    diet_type = ChoiceArrayField(
        models.CharField(
            choices=DIET_TYPES,
            max_length=100,
            blank=True,
            null=True
        ),
        blank=True,
        null=True
    )
    difficulty = models.IntegerField(choices=DIFFICULTY)
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    serves = models.PositiveIntegerField()
    ingredients = models.TextField()
    method = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User,
        related_name='recipe_likes',
        blank=True
    )

    class Meta:
        """
        Ordering of receipes by their creation dates in descending order
        """
        ordering = ['-created_on']

    def __str__(self):
        """ Returns the recipe title as a string """
        return self.title

    def diet_types(self):
        """ Returns the diet types joined as a string """
        return ', '.join(self.diet_type)

    def number_of_likes(self):
        """ Returns the total number of likes for each recipe """
        return self.likes.count()


class Comment(models.Model):
    """ Model for comments """
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(verbose_name="")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Ordering of comments by their creation dates in ascending order
        """
        ordering = ['created_on']

    def __str__(self):
        """ Returns commnent body and auther name """
        return f"Comment {self.body} by {self.name}"

    def date_format_created_on(self):
        """ Date formatting for creation dates """
        return self.created_on.strftime('%d %b %Y')
