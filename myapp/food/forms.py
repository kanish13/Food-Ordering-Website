from django.forms import fields
from django import forms
from .models import Item

class Itemdetail(forms.ModelForm):
    class Meta:
        model=Item
        fields="__all__"