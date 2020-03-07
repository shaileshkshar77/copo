from django import forms
from . import models

class Createdata(forms.ModelForm):
    class Meta:
        model=models.Copo
        fields=["id","name","slug","email","mobile","designation","course_code"]