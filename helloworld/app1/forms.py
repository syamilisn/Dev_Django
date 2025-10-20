from django import forms
from . models import Intro
class IntroForm(forms.ModelForm):
    class Meta:
        model = Intro
        fields = ['text']
        labels = {'text':''}