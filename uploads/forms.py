from django import forms
from .models import Dataset

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ['title', 'file']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'dataset-name',
                'placeholder': 'Nama Dataset',
                'required': True
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control-file dataset-input',
                'id': 'upload-dataset',
                'required': True
            }),
        }

