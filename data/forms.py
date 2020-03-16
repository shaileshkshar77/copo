from django import forms
from . import models

class Marks_form(forms.ModelForm):
    class Meta:
        model=models.Marks
        fields=["course_code","usn","name","cie1","cie2","cie3","quiz1","quiz2","quiz3","experiental_learning","see","survey"]