from django.contrib import admin
from .models import Category, Post

# User.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    
admin.site.register(Category, CategoryAdmin)

# Post.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']

admin.site.register(Post, PostAdmin)