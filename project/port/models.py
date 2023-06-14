from django.db import models

# Create your models here.

class formdata(models.Model):
    uname=models.CharField(max_length=10)
    em=models.EmailField(max_length=50)
    num=models.CharField(max_length=10)
    feedback=models.CharField(max_length=100)

    def __str__(self):
       return self.uname
