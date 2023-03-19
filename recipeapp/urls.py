from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path(
        'recipe/<slug:slug>/',
        views.RecipeDetail.as_view(), name='recipe_detail'
        ),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('post_recipe/', views.PostRecipe.as_view(), name='post_recipe'),
]
