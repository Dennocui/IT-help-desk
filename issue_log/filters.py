from . models import IssueLog

import django_filters
from django_filters import DateRangeFilter, DateFilter
from django_filters.widgets import RangeWidget

class IssueLogFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='trip_date',lookup_expr=('gt'),) 
    end_date = DateFilter(field_name='trip_date',lookup_expr=('lt'))
    date_range = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'date'}),field_name='trip_date', label='Date Range')

    class Meta:
        model= IssueLog
        fields = ['user', 'personel_assinged', 'issue_date', 'due_date', 'priority', 'status','category', 'sub_category', 'mini_category']

    # def __init__(self, *args, **kwargs):
    #        super(TripFilter, self).__init__(*args, **kwargs)
    #    self.filters['posttrips__debreif_status'].label = "Debreif Status"