
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
from .filters import IssueLogFilter
# Create your views here.

@login_required(login_url="/login/")
def issue_list(request):

    issues = IssueLog.objects.all()

    issues_filters = IssueLogFilter(request.GET, queryset=issues)
    issues_filter_qs =issues_filters.qs

    page = request.GET.get('page', 1)

    paginator = Paginator(issues_filter_qs , 10)

    try:
        issues_filter = paginator.page(page)
    except PageNotAnInteger:
        issues_filter = paginator.page(1)
    except EmptyPage:
        issues_filter = paginator.page(paginator.num_pages)


    context = {
        "issues": issues,
        "issues_filters": issues_filters,
        "issues_filter":issues_filter,
    }
    context['segment'] = 'issues'

    html_template = loader.get_template( 'issue_log/issue_log_list.html' )
    return HttpResponse(html_template.render(context, request))

class CreateIssue(CreateView):
    model = IssueLog
    template_name = 'issue_log/create.html'
    form_class =  IssueLogForm 
    success_url = reverse_lazy('issue_log:issue-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


 