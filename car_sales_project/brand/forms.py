from django import forms
from .models import brands

class BrandForm(forms.ModelForm):
    class Meta:
        model = brands
        fields = '__all__'