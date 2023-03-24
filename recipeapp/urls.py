from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('recipes/browse/', views.RecipeList.as_view(), name='browse_recipes'),
    path(
        'recipe/<slug:slug>/',
        views.RecipeDetail.as_view(), name='recipe_detail'
        ),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
    path(
        'recipe/<slug:slug>/update/',
        views.UpdateRecipe.as_view(), name='update_recipe'
        ),
    path(
        'recipe/<slug:slug>/delete/',
        views.DeleteRecipe.as_view(), name='delete_recipe'
        ),
    path(
        'comment/<int:pk>/update/',
        views.UpdateComment.as_view(), name='update_comment'
        ),
    path(
        'comment/<int:pk>/delete/',
        views.DeleteComment.as_view(), name='delete_comment'
        ),
    path(
        'my-recipes/',
        views.MyRecipes.as_view(), name='my_recipes'
        ),
    path(
        'my-favourites/',
        views.MyFavourites.as_view(), name='my_favourites'
        ),
    path('recipe/post', views.PostRecipe.as_view(), name='post_recipe'),
]
