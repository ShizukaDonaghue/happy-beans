from django.test import TestCase
from .forms import CommentForm, RecipeForm


class TestCommentForm(TestCase):
    def test_commentform_valid(self):
        """ Test if comment form is valid """
        form = CommentForm({'body': 'I love this!'})
        self.assertTrue(form.is_valid())

    def test_commentform_invalid(self):
        """ Test if comment form is invalid """
        form = CommentForm({'body': ''})
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')
        self.assertFalse(form.is_valid())


class TestRecipeForm(TestCase):
    def test_recipeform_valid(self):
        """ Test if recipe form is valid """
        form = RecipeForm({
            'title': 'Chicken Curry',
            'description': 'Yummy curry',
            'meal_type': '2',
            'main_ingredient': '1',
            'difficulty': '0',
            'prep_time': '10',
            'cook_time': '10',
            'serves': '4',
            'ingredients': 'Curry',
            'method': 'Cook curry',
            'status': '1',
        })
        self.assertTrue(form.is_valid())

    def test_recipeform_invalid(self):
        """ Test if recipe form is invalid """
        form = RecipeForm({
            'title': '',
            'description': '',
            'meal_type': '',
            'main_ingredient': '',
            'difficulty': '',
            'prep_time': '',
            'cook_time': '',
            'serves': '',
            'ingredients': '',
            'method': '',
            'status': '',
        })
        self.assertIn('title', form.errors.keys())
        self.assertIn('description', form.errors.keys())
        self.assertIn('meal_type', form.errors.keys())
        self.assertIn('main_ingredient', form.errors.keys())
        self.assertIn('difficulty', form.errors.keys())
        self.assertIn('prep_time', form.errors.keys())
        self.assertIn('cook_time', form.errors.keys())
        self.assertIn('serves', form.errors.keys())
        self.assertIn('ingredients', form.errors.keys())
        self.assertIn('method', form.errors.keys())
        self.assertIn('status', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')
        self.assertEqual(
            form.errors['meal_type'][0], 'This field is required.')
        self.assertEqual(
            form.errors['main_ingredient'][0], 'This field is required.')
        self.assertEqual(
            form.errors['difficulty'][0], 'This field is required.')
        self.assertEqual(
            form.errors['prep_time'][0], 'This field is required.')
        self.assertEqual(
            form.errors['cook_time'][0], 'This field is required.')
        self.assertEqual(form.errors['serves'][0], 'This field is required.')
        self.assertEqual(
            form.errors['indredients'][0], 'This field is required.')
        self.assertEqual(form.errors['method'][0], 'This field is required.')
        self.assertEqual(form.errors['status'][0], 'This field is required.')
        self.assertFalse(form.is_valid())
