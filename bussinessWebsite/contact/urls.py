from django.urls import path
from . import views

urlpatterns = [
    # Contact.
    path('', views.contact, name='contact')
]
