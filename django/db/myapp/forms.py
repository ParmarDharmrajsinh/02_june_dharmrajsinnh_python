from django import forms
from .models import *

class student(forms.ModelForm):
    class Meta:#data about data
        model=product
        fields='__all__'
