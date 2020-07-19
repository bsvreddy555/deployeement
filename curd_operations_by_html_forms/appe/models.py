from django.db import models

# Create your models here.
class Employee_model(models.Model):
    f_name=models.CharField(max_length=100)
    l_name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=50)
    salary=models.FloatField()
    experience=models.FloatField()
    location=models.CharField(max_length=50,null=True,blank=True)
    company=models.CharField(max_length=50)