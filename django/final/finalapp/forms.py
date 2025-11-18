from django import forms
from .models import *

class UserinfoForm(forms.ModelForm):
    class Meta:
        model=Userinfo
        fields="__all__"

class mynotesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields=['title','desc','file','category']


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"