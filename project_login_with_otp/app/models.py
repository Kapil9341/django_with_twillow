from django.db import models
from django.core import validators  

# Create your models here.
class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=70)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    pass1 = models.CharField(max_length=50)
    pass2 = models.CharField(max_length=50)
    
    def __str__(self):
        return self.fname

    #     fname = models.CharField(max_length= 50)
    # roll = models.IntegerField()
    # marks = models.IntegerField()
    # city = models.CharField(max_length= 70)
# id = models.AutoField(primary_key=True

class User(models.Model):
    name = models.CharField(max_length=70,blank=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name