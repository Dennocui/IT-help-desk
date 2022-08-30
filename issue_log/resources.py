from django.contrib import admin
from django.db.models import Sum, Count, Q, F, Func, fields
from django.db import models


from import_export import resources
from import_export.fields import Field

from . models import IssueLog

class IssueLogResource(resources.ModelResource):
    
    user = Field(column_name = 'User', attribute='user') 
    personel_assinged = Field(column_name = 'Personel Assinged', attribute='personel_assinged')
    equipment_type__name = Field(column_name = 'Equipment Type', attribute='equipment_type__name')
    equipment_make__name= Field(column_name ='Equipment Make', attribute='equipment_make__name')
    equipment_brand__name= Field(column_name ='Equipment Brand', attribute='equipment_brand__name')
    issue_date = Field(column_name = 'Issue Date', attribute='issue_date')
    due_date= Field(column_name = 'Due Date', attribute='due_date')
    issue = Field(column_name = 'Issue', attribute='issue')
    priority = Field(column_name = 'Priority', attribute='priority')
    status = Field(column_name = 'Status', attribute='status')
    comments = Field(column_name = 'Comments', attribute='comments')


    class Meta:
        model = IssueLog
        fields = ('personel_assinged','user','equipment_type__name', 'equipment_make__name','equipment_brand__name' ,'issue', 'priority','issue_date', 'due_date','status', 'comments')
        export_order = ('personel_assinged','user','equipment_type__name', 'equipment_make__name','equipment_brand__name' ,'issue','priority', 'issue_date', 'due_date', 'status','comments')