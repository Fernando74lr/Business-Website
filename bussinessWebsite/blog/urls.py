from django.urls import path
from . import views

urlpatterns = [
    # Blog.
    path('', views.blog, name='blog')
]
