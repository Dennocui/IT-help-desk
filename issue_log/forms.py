from django import forms
from .models import IssueLog

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .widgets import FengyuanChenDatePickerInput
from django.contrib.admin import widgets

class DateInput(forms.DateInput):
    input_type = 'date'

class IssueLogForm(forms.ModelForm):
    # personel_assinged = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    issue_date = forms.DateField(input_formats=['%d/%m/%Y'], widget=FengyuanChenDatePickerInput())
    due_date = forms.DateField(input_formats=['%d/%m/%Y'], widget=FengyuanChenDatePickerInput())
    # personel_assinged = forms.Select(widget=forms.HiddenInput())
    class Meta:
        model = IssueLog
        fields = ['user','category', 'sub_category', 'mini_category','issue','personel_assinged','priority','issue_date','due_date','comments','status']
        widgets = {
          'comments': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }
      
      

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(IssueLogForm, self).__init__(*args, **kwargs)
        self.fields['personel_assinged'].initial = self.request.user
        # self.fields['issue_date'].widget = widgets.AdminDateWidget()
        # self.fields['due_date'].widget = widgets.AdminDateWidget()
        # self.fields['personel_assinged'].widget.attrs['readonly'] = 'readonly'    

        

                    