# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
    path("chaining/", include('smart_selects.urls')),
    path("category/", include("category.urls")),
    path("issue_log/", include("issue_log.urls")),
    
    
    path("", include("app.urls")),             # UI Kits Html files
    
]
