from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Copo(models.Model):
    id=models.CharField( max_length=15,primary_key=True)
    name=models.CharField( max_length=50)
    slug=models.SlugField()
    email=models.CharField( max_length=50)
    mobile=models.CharField( max_length=50)
    designation=models.CharField( max_length=20)
    course_code=models.CharField( max_length=15)
    
    #add picture

    def __str__(self):
        return self.name

    #def snip(self):
        #return self.body[:20]+'...'
