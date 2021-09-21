from django import forms
from .models import IssueLog

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class IssueLogForm(forms.ModelForm):
    class Meta:
        model = IssueLog
        fields = ['user','category', 'sub_category', 'mini_category','issue','personel_assinged','priority','issue_date','due_date','comments','status']
      

        

                    