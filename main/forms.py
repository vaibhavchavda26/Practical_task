from django.forms import ModelForm
from main.models import Opportunity
from django import forms


class OpportunityCreateForm(ModelForm):

    dob = forms.DateField(widget=forms.DateInput())

    class Meta:
        model = Opportunity
        fields = "__all__"
