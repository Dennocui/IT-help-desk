from django.contrib import admin
from django.db.models import Sum, Count, Q, F, Func, fields
from django.db import models


from import_export import resources
from import_export.fields import Field

from . models import IssueLog

class IssueLogResource(resources.ModelResource):
    
    user = Field(column_name = 'User', attribute='user') 
    personel_assinged = Field(column_name = 'Personel Assinged', attribute='personel_assinged')
    category__name = Field(column_name = 'Category', attribute='category__name')
    sub_category__name= Field(column_name ='Sub-Category', attribute='sub_category__name')
    mini_category__name= Field(column_name ='Mini-Category', attribute='mini_category__name')
    issue_date = Field(column_name = 'Issue Date', attribute='issue_date')
    due_date= Field(column_name = 'Due Date', attribute='due_date')
    issue = Field(column_name = 'Issue', attribute='issue')
    priority = Field(column_name = 'Priority', attribute='priority')
    status = Field(column_name = 'Status', attribute='status')
    comments = Field(column_name = 'Comments', attribute='comments')


    class Meta:
        model = IssueLog
        fields = ('personel_assinged','user','category__name', 'sub_category__name','mini_category__name' ,'issue', 'priority','issue_date', 'due_date','status', 'comments')
        export_order = ('personel_assinged','user','category__name', 'sub_category__name','mini_category__name' ,'issue','priority', 'issue_date', 'due_date', 'status','comments')