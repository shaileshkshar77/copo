from django.db import models
from django.contrib.auth.models import User

class Info(models.Model):
    usn=models.CharField( max_length=15)
    name=models.CharField( max_length=50)

    def __str__(self):
        return self.name

class Courses(models.Model):
    course_code=models.CharField( max_length=15)

    def __str__(self):
        return self.course_code

# Create your models here.
class Marks(models.Model):
    usn=models.ForeignKey(Info,on_delete=models.CASCADE)
    course_code=models.ForeignKey(Courses,on_delete=models.CASCADE)
    Co1_cie1=models.IntegerField()
    Co2_cie1=models.IntegerField()
    Co3_cie1=models.IntegerField()
    Co4_cie1=models.IntegerField()
    Co1_cie2=models.IntegerField()
    Co2_cie2=models.IntegerField()
    Co3_cie2=models.IntegerField()
    Co4_cie2=models.IntegerField()
    Co1_cie3=models.IntegerField()
    Co2_cie3=models.IntegerField()
    Co3_cie3=models.IntegerField()
    Co4_cie3=models.IntegerField()
    Co1_quiz1=models.IntegerField()
    Co2_quiz1=models.IntegerField()
    Co3_quiz1=models.IntegerField()
    Co4_quiz1=models.IntegerField()
    Co1_quiz2=models.IntegerField()
    Co2_quiz2=models.IntegerField()
    Co3_quiz2=models.IntegerField()
    Co4_quiz2=models.IntegerField()
    Co1_quiz3=models.IntegerField()
    Co2_quiz3=models.IntegerField()
    Co3_quiz3=models.IntegerField()
    Co4_quiz3=models.IntegerField()
    experiental_learning=models.IntegerField()
    see=models.IntegerField()
    survey=models.IntegerField()
    
    #add picture

    def __str__(self):
        return self.usn

class Max_Marks(models.Model):
    course_code=models.ForeignKey(Courses,on_delete=models.CASCADE)
    Co1_cie1=models.IntegerField()
    Co2_cie1=models.IntegerField()
    Co3_cie1=models.IntegerField()
    Co4_cie1=models.IntegerField()
    Co1_cie2=models.IntegerField()
    Co2_cie2=models.IntegerField()
    Co3_cie2=models.IntegerField()
    Co4_cie2=models.IntegerField()
    Co1_cie3=models.IntegerField()
    Co2_cie3=models.IntegerField()
    Co3_cie3=models.IntegerField()
    Co4_cie3=models.IntegerField()
    Co1_quiz1=models.IntegerField()
    Co2_quiz1=models.IntegerField()
    Co3_quiz1=models.IntegerField()
    Co4_quiz1=models.IntegerField()
    Co1_quiz2=models.IntegerField()
    Co2_quiz2=models.IntegerField()
    Co3_quiz2=models.IntegerField()
    Co4_quiz2=models.IntegerField()
    Co1_quiz=models.IntegerField()
    Co2_quiz3=models.IntegerField()
    Co3_quiz3=models.IntegerField()
    Co4_quiz3=models.IntegerField()
    experiental_learning=models.IntegerField()
    see=models.IntegerField()
    survey=models.IntegerField()
    
    #add picture

    def __str__(self):
        return self.course_code
    
class Sum(models.Model):
    course_code=models.ForeignKey(Courses,on_delete=models.CASCADE)
    Co1=models.IntegerField()
    Co2=models.IntegerField()
    Co3=models.IntegerField()
    Co4=models.IntegerField()

    def __str__(self):
        return self.course_code

class Max_Sum(models.Model):
    course_code=models.ForeignKey(Courses,on_delete=models.CASCADE)
    Co1=models.IntegerField()
    Co2=models.IntegerField()
    Co3=models.IntegerField()
    Co4=models.IntegerField()

    def __str__(self):
        return self.course_code

class Co(models.Model):
    course_code=models.ForeignKey(Courses,on_delete=models.CASCADE)
    Co1=models.IntegerField()
    Co2=models.IntegerField()
    Co3=models.IntegerField()
    Co4=models.IntegerField()

    def __str__(self):
        return self.course_code

