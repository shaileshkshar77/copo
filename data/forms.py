from django import forms
from . import models

class Marks_form(forms.ModelForm):
    class Meta:
        model=models.Marks
        fields=["course_code","usn","Co1_cie1","Co2_cie1","Co3_cie1","Co4_cie1","Co1_cie2","Co2_cie2","Co3_cie2","Co4_cie2","Co1_cie3","Co2_cie3","Co3_cie3","Co4_cie3","Co1_quiz1","Co2_quiz1","Co3_quiz1","Co4_quiz1","Co1_quiz2","Co2_quiz2","Co3_quiz2","Co4_quiz2","Co1_quiz3","Co2_quiz3","Co3_quiz3","Co4_quiz3","experiental_learning","see","survey"]

class Marks_Info(forms.ModelForm):
    class Meta:
        model=models.Info
        fields=["name","usn"]


class Marks_Courses(forms.ModelForm):
    class Meta:
        model=models.Courses
        fields=["course_code"]