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
        'update-recipe/<slug:slug>/',
        views.UpdateRecipe.as_view(), name='update_recipe'
        ),
    path(
        'delete-recipe/<slug:slug>/',
        views.DeleteRecipe.as_view(), name='delete_recipe'
        ),
    path(
        'update-comment/<int:pk>/',
        views.UpdateComment.as_view(), name='update_comment'
        ),
]
