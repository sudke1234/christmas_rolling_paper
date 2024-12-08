
from django import forms
from .models import Decoration

class DecorationForm(forms.ModelForm):
    class Meta:
        model = Decoration
        fields = ['title', 'content']
