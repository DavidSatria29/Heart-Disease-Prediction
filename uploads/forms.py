from django import forms
from .models import Dataset

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ['title', 'file']

