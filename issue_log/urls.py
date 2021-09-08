from django.urls import path

from . import views


app_name = "issue_log"

urlpatterns = [
    
    path('issue-list', views.issue_list, name='issue-list'),


    
]
