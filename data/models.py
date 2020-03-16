from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Marks(models.Model):
    course_code=models.CharField( max_length=15)
    usn=models.CharField( max_length=15,primary_key=True)
    name=models.CharField( max_length=50)
    cie1=models.IntegerField()
    cie2=models.IntegerField()
    cie3=models.IntegerField()
    quiz1=models.IntegerField()
    quiz2=models.IntegerField()
    quiz3=models.IntegerField()
    experiental_learning=models.IntegerField()
    see=models.IntegerField()
    survey=models.IntegerField()
    
    #add picture

    def __str__(self):
        return self.name