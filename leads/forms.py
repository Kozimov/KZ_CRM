from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "ismi",
            "familiyasi",
            "yoshi",
            "agent"
        )

class LeadForm(forms.Form):
    ismi = forms.CharField(max_length=20)
    familiyasi = forms.CharField(max_length=20)
    yoshi = forms.IntegerField(min_value=0)

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}