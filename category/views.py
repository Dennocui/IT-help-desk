
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template


from django.views.generic import CreateView, DeleteView, UpdateView, DetailView

from .models import Category, SubCategory,MiniCategory

# Create your views here.

@login_required(login_url="/login/")
def category_list(request):

    categories = SubCategory.objects.select_related()

    context = {
        "categories": categories,
    }
    context['segment'] = 'category-main'

    html_template = loader.get_template( 'category/category_list.html' )
    return HttpResponse(html_template.render(context, request))


    

@login_required(login_url="/login/")
def sub_category_list(request):
    
    context = {}
    context['segment'] = 'category-sub'

    html_template = loader.get_template( 'category/category_list.html' )
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def mini_category_list(request):
    
    context = {}
    context['segment'] = 'category-mini'

    html_template = loader.get_template( 'category/category_list.html' )
    return HttpResponse(html_template.render(context, request))



