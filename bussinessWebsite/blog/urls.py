from django.urls import path
from . import views

urlpatterns = [
    # Blog.
    path('', views.blog, name='blog'),
    # Dynamic field.
    path('category/<int:category_id>/', views.category, name="category")
]
