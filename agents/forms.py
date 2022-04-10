from django import forms
from leads.models import *

class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            "user",
        )