from django.contrib import admin
from .models import Category, Post, Comment
# Register your models here.

@admin.register(Category)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Post)
class PostAdminModel(admin.ModelAdmin):
    list_display = ['title','author','category','created_at','image']
    
@admin.register(Comment)
class CommentAdminModel(admin.ModelAdmin):
    list_display = ['commenter','post', 'created_at']
    