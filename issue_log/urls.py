from django.urls import path

from . import views


app_name = "issue_log"

urlpatterns = [
    
    path('issue-list', views.issue_list, name='issue-list'),
    path('create-isssue', views.CreateIssue.as_view(), name='create-issue'),
    
]
