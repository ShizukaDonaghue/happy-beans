from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('browse-recipes/', views.RecipeList.as_view(), name='browse_recipes'),
    path(
        'recipe/<slug:slug>/',
        views.RecipeDetail.as_view(), name='recipe_detail'
        ),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
    path('post-recipe/', views.PostRecipe.as_view(), name='post_recipe'),
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
        'myrecipes/',
        views.MyRecipes.as_view(), name='my_recipes'
        ),
]
