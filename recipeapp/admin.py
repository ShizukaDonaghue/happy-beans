from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """ Admin panel settings for recipes """
    search_fields = ['title', 'description', 'author']
    list_display = (
        'title',
        'author',
        'description',
        'status',
        'created_on',
        'updated_on'
    )
    list_filter = ('status', 'created_on', 'updated_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'method')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Admin panel settings for comments """
    list_display = ('recipe', 'name', 'body', 'created_on', 'updated_on')
    list_filter = ('name', 'created_on', 'updated_on')
    search_fields = ['name', 'email', 'body']
