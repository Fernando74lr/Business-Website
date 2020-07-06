from django.urls import path
from . import views

urlpatterns = [
    # Services.
    path('services/', views.services, name='services')
]
