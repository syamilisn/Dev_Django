from dataclasses import field
from django import forms
from . models import Measure
class MeasureForm(forms.ModelForm):
    class Meta:
        model = Measure
        fields = ['weight','waist','hip','bust','arms','thigh','bottom','date']
        labels = {
            'weight':'Weight:',
            'waist':'Waist :',
            'hip':'Hip   :',
            'bust':'Bust  :',
            'arms':'Arms  :',
            'thigh':'Thigh :',
            'bottom':'Bottom:',
            'date':'Date  :'
        }