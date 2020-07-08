from django.contrib import admin
from .models import Category, Post

# User.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    
admin.site.register(Category, CategoryAdmin)

# Post.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['title', 'author', 'published', 'post_categories']
    ordering = ['author', 'published']
    search_fields = ['title', 'content', 'author__username', 'categories__name']
    list_filter = ['author__username', 'categories__name']

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'categories'

admin.site.register(Post, PostAdmin)