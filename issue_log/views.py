
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from .models import IssueLog

# Create your views here.

@login_required(login_url="/login/")
def issue_list(request):

    issues = IssueLog.objects.all()

    context = {
        "issues": issues,
    }
    context['segment'] = 'issues'

    html_template = loader.get_template( 'issue_log/issue_log_list.html' )
    return HttpResponse(html_template.render(context, request))