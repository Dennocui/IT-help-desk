from django.urls import path

from . import views


app_name = "category"

urlpatterns = [
    
    path('category-list', views.category_list, name='category-list'),


    
]
