from django.urls import path
from . import views

urlpatterns = [
    # Core.
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('sample/', views.sample, name='sample'),
    path('services/', views.services, name='services'),
    path('store/', views.store, name='store'),
]
