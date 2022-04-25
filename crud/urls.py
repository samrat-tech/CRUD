from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_details', views.add_details, name="add_details"),
    path('edit/<int:roll>', views.edit, name="edit_data"),
    path('delete/<int:roll>', views.delete, name="delete")
]