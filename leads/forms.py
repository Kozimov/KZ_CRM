from dataclasses import fields
from django import forms
from .models import Lead

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "ismi",
            "familiyasi",
            "yoshi",
            "agent",
        )


class LeadForm(forms.Form):
    ismi = forms.CharField(max_length=20)
    familiyasi = forms.CharField(max_length=20)
    yoshi = forms.IntegerField(min_value=0)