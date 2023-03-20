from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path(
        'recipe/<slug:slug>/',
        views.RecipeDetail.as_view(), name='recipe_detail'
        ),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('post-recipe/', views.PostRecipe.as_view(), name='post_recipe'),
    path(
        'recipe/<slug:slug>/update/',
        views.UpdateRecipe.as_view(), name='update_recipe'
        ),
    path(
        'recipe/<slug:slug>/delete/',
        views.DeleteRecipe.as_view(), name='delete_recipe'
        ),
]
