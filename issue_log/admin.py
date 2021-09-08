from django.contrib import admin

# Register your models here.
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter


from .models import IssueLog

# admin.site.register(IssueLog)


@ admin.register(IssueLog)
class IssueLogAdmin(admin.ModelAdmin):
    # resource_class = IssueLogResource
    list_display = ('user','category', 'sub_category','mini_category' ,'issue', 'personel_assinged','priority', 'status','issue_date', 'due_date', 'comments')
    list_filter = (('issue_date', DateRangeFilter,), ('category'),('sub_category'),
                   ('status'), )
    ordering = ('issue_date', )
    # date_hierarchy = 'trip_date'
    search_fields = ('issue',)
    # actions = ["export_as_csv"]
    fieldsets = (
        ('Basic Information', {
            #   'description': "Player Bio Data.", ('customer', ), ('tonnage', 'zone', 'location'), ('truck', 'driver')
            'fields': (
                ('user','personel_assinged'),('category','sub_category','mini_category'),('issue','priority'),('issue_date','due_date'),('status',),('comments')  
                       )}),

    )
