
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.urls import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.views.generic.edit import CreateView
from .models import IssueLog
from .forms import IssueLogForm

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

class CreateIssue(CreateView):
    model = IssueLog
    template_name = 'issue_log/create.html'
    form_class =  IssueLogForm 
    success_url = reverse_lazy('issue_log:issue-list')


 