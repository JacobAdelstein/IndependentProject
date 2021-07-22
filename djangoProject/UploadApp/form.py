from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    Description = forms.CharField(widget=forms.Textarea( attrs={'class': 'form-control', 'placeholder': 'Text goes here', 'rows': '4', 'cols': '10'}))

    class Meta:
        model = Image
        fields = ("Description", "image",)



