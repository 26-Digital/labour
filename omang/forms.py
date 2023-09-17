from django import forms
from .models import Omang

class OmangForm(forms.ModelForm):
    class Meta:
        model = Omang
        fields = '__all__'