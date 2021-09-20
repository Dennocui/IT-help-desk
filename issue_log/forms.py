from django import forms
from .models import IssueLog

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class IssueLogForm(forms.ModelForm):
    class Meta:
        model = IssueLog
        fields = ('user','category', 'sub_category', 'mini_category','issue','personel_assinged','priority','issue_date','due_date','comments','status')
        widgets = {
            'invoice_no': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'subby_invoice_no': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'user':forms.Select(attrs={'class': 'form-control'}),
            'category':forms.Select(attrs={'class': 'form-control'}), 
            'sub_category':forms.Select(attrs={'class': 'form-control'}), 
            'mini_category':forms.Select(attrs={'class': 'form-control'}),
            'issue': forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}), 
            'personel_assinged':forms.Select(attrs={'class': 'form-control'}), 
            'priority':forms.Select(attrs={'class': 'form-control'}),
            'issue_date': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}), 
            'due_date': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}), 
            'comments': forms.Textarea(attrs={'type': 'text', 'class': 'form-control'}), 
            'status': forms.Select(attrs={'class': 'form-control'}), 
        }

        

                    