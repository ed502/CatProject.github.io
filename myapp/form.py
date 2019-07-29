from django import forms
from .models import Cat

class CatPost(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'image', 'latitude', 'longitude']