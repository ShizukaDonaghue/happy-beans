from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from django.views import generic, View
from django.urls import reverse_lazy
from .models import Recipe
from .forms import CommentForm, RecipeForm


class RecipeList(generic.ListView):
    """
    Displays a list of 9 recipes per page
    Recipes are ordered by their creation dates in descending order
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 9


class RecipeDetail(View):
    """
    Displays the detail of a recipe and comments
    Includes comment form if the user is logged in
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Get method to diplay the details
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Post method used to post a comment
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


class RecipeLike(View):
    """
    Post method to like or unlike the recipe
    """
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class PostRecipe(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """
    Displays the recipe entry form when user is logged in
    Allows the user to post a recipe
    """
    model = Recipe
    template_name = 'post_recipe.html'
    form_class = RecipeForm
    success_url = reverse_lazy('home')
    success_message = (
        "Thank you! %(calculated_field)s has been added successfully!"
        )

    def form_valid(self, form):
        """
        Checks if the form is valid
        Inserts the user id as a field and set it as the author
        Adds the recipe title as the slug
        """
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """
        Overrides the get_success_message () to include the recipe title
        in the success_message
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )


class UpdateRecipe(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, generic.UpdateView
        ):
    """
    Allows the user to update their recipe when logged in
    """
    model = Recipe
    template_name = 'post_recipe.html'
    form_class = RecipeForm
    success_url = reverse_lazy('home')
    success_message = (
        "Thank you! %(calculated_field)s has been updated successfully!"
    )

    def form_valid(self, form):
        """
        Checks if the form is valid
        Inserts the user id as a field and set it as the author
        Adds the recipe title as the slug
        """
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    def test_func(self):
        """
        Tests if the user is the author of the recipe
        """
        recipe = self.get_object()
        return recipe.author == self.request.user

    def get_success_message(self, cleaned_data):
        """
        Overrides the get_success_message () to include the recipe title
        in the success_message
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )


class DeleteRecipe(
        LoginRequiredMixin,
        UserPassesTestMixin,
        generic.DeleteView
        ):
    """
    Allows the user to delete their own recipe when logged in
    """
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('home')
    success_message = "Recipe has been deleted successfuly. Thanks."

    def test_func(self):
        """
        Tests if the user is the author of the recipe
        """
        recipe = self.get_object()
        return recipe.author == self.request.user

    def delete(self, request, *args, **kwargs):
        """
        Displays confirmation that recipe has been deleted successfully
        """
        messages.success(self.request, self.success_message)
        return super(DeleteRecipe, self).delete(request, *args, **kwargs)
