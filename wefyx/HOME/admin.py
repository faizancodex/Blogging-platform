from django.contrib import admin
from .models import Category, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_category', 'created_at', 'read_count')
    list_filter = ('post_category', 'created_at', 'author')
    search_fields = ('post_title', 'description')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name',)
    search_fields = ('cat_name',)