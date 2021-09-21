from django import forms
from .models import IssueLog

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class IssueLogForm(forms.ModelForm):
    # personel_assinged = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    issue_date = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))
    due_date = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))
    class Meta:
        model = IssueLog
        fields = ['user','category', 'sub_category', 'mini_category','issue','personel_assinged','priority','issue_date','due_date','comments','status']
      

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(IssueLogForm, self).__init__(*args, **kwargs)
        self.fields['personel_assinged'].initial = self.request.user
        # self.fields['personel_assinged'].widget.attrs['readonly'] = 'readonly'    

        

                    