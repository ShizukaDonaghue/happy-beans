from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django_filters.views import FilterView
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from django.views import generic, View
from django.urls import reverse_lazy
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm
from .filters import RecipeFilter


class Home(generic.TemplateView):
    """
    Displays the home page
    """
    template_name = 'index.html'


class RecipeList(FilterView):
    """
    Displays a list of 9 recipes per page
    Recipes are ordered by their creation dates in descending order
    """
    model = Recipe
    template_name = 'browse_recipes.html'
    filterset_class = RecipeFilter
    paginate_by = 9

    def get_context_data(self, **kwargs):
        """
        Returns a filtered list of recipes to display
        Adds pagination to the filtered list
        Code reference: Django filter and pagination
        https://www.youtube.com/watch?v=dkJ3uqkdCcY
        """
        context = {}
        filtered_recipes = RecipeFilter(
            self.request.GET,
            queryset=Recipe.objects.filter(status=1).order_by('-created_on')
        )
        context['filtered_recipes'] = filtered_recipes
        paginated_filtered_recipes = Paginator(filtered_recipes.qs, 9)
        page_number = self.request.GET.get('page')
        recipe_page_obj = paginated_filtered_recipes.get_page(page_number)
        context['recipe_page_obj'] = recipe_page_obj
        return context


class RecipeDetail(View):
    """
    Displays the detail of a recipe and comments
    Includes comment form if the user is logged in
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Get method to display the details
        """
        queryset = Recipe.objects.all()
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
        Post method to post a comment
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
    Allows the user to like or unlike a recipe when logged in
    """
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class RecipeAuthorMixin(LoginRequiredMixin):
    """
    A mixin to set the user as the author of the recipe
    """
    def form_valid(self, form):
        """
        Checks if the form is valid
        Inserts the user id as a field and set it as the author of the recipe
        Adds the recipe title as the slug
        """
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class RecipeAuthorTestMixin(UserPassesTestMixin):
    """
    A mixin to test if the user is the author of the recipe
    to ensure only the recipe author can update or delete the recipe
    """
    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user


class RecipeMessageMixin(SuccessMessageMixin):
    """
    A mixin to override the get_success_message() to include the recipe title
    """
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            recipe_title=self.object.title,
        )


class PostRecipe(RecipeAuthorMixin, RecipeMessageMixin, generic.CreateView):
    """
    Allows the user to post a recipe when logged in
    """
    model = Recipe
    template_name = 'post_recipe.html'
    form_class = RecipeForm
    success_message = (
        "Thank you! %(recipe_title)s has been added successfully!"
        )

    def get_success_url(self):
        return reverse_lazy('recipe_detail', args=[self.object.slug])


class UpdateRecipe(
        RecipeAuthorMixin, RecipeAuthorTestMixin,
        RecipeMessageMixin, generic.UpdateView
        ):
    """
    Allows the user to update their recipe when logged in
    """
    model = Recipe
    template_name = 'update_recipe.html'
    form_class = RecipeForm
    success_message = (
        "Thank you! %(recipe_title)s has been updated successfully!"
    )

    def get_success_url(self):
        return reverse_lazy('recipe_detail', args=[self.object.slug])


class DeleteRecipe(
        LoginRequiredMixin, RecipeAuthorTestMixin, generic.DeleteView
        ):
    """
    Allows the user to delete their own recipe when logged in
    """
    model = Recipe
    success_url = reverse_lazy('browse_recipes')
    success_message = "Recipe has been deleted successfuly. Thanks."

    def delete(self, request, *args, **kwargs):
        """
        Deletes the recipe
        Displays confirmation that it has been deleted successfully
        Code source: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.success(self.request, self.success_message)
        return super(DeleteRecipe, self).delete(request, *args, **kwargs)


class MyFavourites(LoginRequiredMixin, generic.ListView):
    """
    Displays a list of recipes liked by the user, 9 recipes per page
    Recipes are ordered by their creation dates in descending order
    """
    model = Recipe
    template_name = 'my_favourites.html'
    paginate_by = 9

    def get_queryset(self):
        return Recipe.objects.filter(
            likes=self.request.user).filter(status=1).order_by('-created_on')


class MyRecipes(LoginRequiredMixin, generic.ListView):
    """
    Displays a list of recipes posted by the user, 9 recipes per page
    Recipes are ordered by their creation dates in descending order
    """
    model = Recipe
    template_name = 'my_recipes.html'
    paginate_by = 9

    def get_queryset(self):
        return Recipe.objects.filter(
            author=self.request.user).order_by('-created_on')


class CommentAuthorMixin(UserPassesTestMixin):
    """
    A mixin to test if the user is the author of the comment
    to ensure only the comment author can update or delete the comment
    """
    def test_func(self):
        comment = self.get_object()
        return comment.name == self.request.user.username


class SetUrlMixin:
    """
    A mixin to set to url to return to when the form is validated successfully
    """
    def get_success_url(self):
        return reverse_lazy('recipe_detail', args=[self.object.recipe.slug])


class UpdateComment(
        LoginRequiredMixin, CommentAuthorMixin,
        SuccessMessageMixin, SetUrlMixin, generic.UpdateView
        ):
    """
    Allows the user to update their comment when logged in
    """
    model = Comment
    template_name = 'update_comment.html'
    form_class = CommentForm
    success_message = "Your comment has been updated successfully."


class DeleteComment(
        LoginRequiredMixin, CommentAuthorMixin, SetUrlMixin, generic.DeleteView
        ):
    """
    Allows the user to delete their comment when logged in
    """
    model = Comment
    form_class = CommentForm
    success_message = "Your comment has been deleted successfully."

    def delete(self, request, *args, **kwargs):
        """
        Deletes the recipe
        Displays confirmation that it has been deleted successfully
        Code source: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.success(self.request, self.success_message)
        return super(DeleteComment, self).delete(request, *args, **kwargs)
