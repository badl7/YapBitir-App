from django import forms
from .models import Yapbitir

class YapbitirForm(forms.ModelForm):
    class Meta:
        model = Yapbitir
        fields = ["title" , "content" , "dateline"]