from django import forms
from .models import *

class YorumOlustur(forms.ModelForm):
    class Meta:
        model = Yorum
        fields = ['rating','description','is_active',]
        labels ={
            'rating':'rating',
            'description':'description',
        },

        widgets = {
            'description':forms.TextInput(attrs={'class':'form-control w-50','placeholder':'Yorumunuz:'}),
            'rating':forms.TextInput(attrs={'class':'form-control w-50','placeholder':'Derece giriniz:'}),
            'is_active':forms.CheckboxInput(attrs={'class':'form-checkbox d-block w-5'}),
        }