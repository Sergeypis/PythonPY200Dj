from django import forms
from django.core.validators import RegexValidator


class ModestContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    # phone = RegexValidator(regex=r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', message="error")
    phone = forms.RegexField(regex=r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')
    message = forms.CharField(widget=forms.Textarea)
