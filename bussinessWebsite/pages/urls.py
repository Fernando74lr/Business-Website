from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path('<int:page_id>/', views.page, name="page")
]
