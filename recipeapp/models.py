from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from cloudinary.models import CloudinaryField
from .validators import textfield_not_empty


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
    (8, 'Vegetable'),
    (9, 'Other')
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
    """
    A model to create and manage recipes:
        Title - recipe title
        Slug - a field used to store and generate valid URL path automatically
        Author - recipe author, assigned by username automatically
        Description - recipe description
        Created_on - recipe creation date, used to organise recipes in order
        Updated_on - recipe update date, used for admin purposes
        Meal_type - meal type such as breakfast & lunch, used for recipe filter
        Main_ingredient - main ingredient of recipe, used for recipe filter
        Diet_type - diet type such as gluten-free, vegetarian & nut-free
        Difficulty - recipe difficulty level, used for recipe filter
        Prep_time - recipe preparation time
        Cook_time - recipe cooking time
        Serves - recipe servings
        Ingredients - all ingredients required
        Method - cooking method
        Image - recipe image, if none provided, a default image is displayed
        Status - recipe status, either draft or published
        Likes - indicating the number of likes by users
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipe_posts'
    )
    description = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    meal_type = models.IntegerField(
        verbose_name="Meal Type", choices=MEAL_TYPE)
    main_ingredient = models.IntegerField(
        verbose_name="Main Ingredient", choices=MAIN_INGREDIENT)
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
    prep_time = models.PositiveIntegerField(verbose_name="Prep Time (mins)")
    cook_time = models.PositiveIntegerField(verbose_name="Cooking Time (mins)")
    serves = models.PositiveIntegerField()
    ingredients = models.TextField(validators=[textfield_not_empty])
    method = models.TextField(validators=[textfield_not_empty])
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User,
        related_name='recipe_likes',
        blank=True
    )

    class Meta:
        """
        Ordering of recipes by their creation dates in descending order
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
    """
    A model to create and manage comments:
        Name - comment author, assigned by username automatically
        Email - user email, assigned by user email automatically
        Body - comment content
        Created_on - comment creation date, used to organise comments in order
        Updated_on - comment update date, used for admin purposes
    """
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
        """ Returns comment body and author name """
        return f"Comment {self.body} by {self.name}"

    def date_format_created_on(self):
        """ Date formatting for creation dates """
        return self.created_on.strftime('%d %b %Y')
