from statistics import mode
from django.db import models

# Create your models here.


class EmployModel(models.Model):
   
    emp_id = models.PositiveBigIntegerField(blank=False,)
    name = models.CharField(blank=False, max_length=100)
    salary = models.FloatField(blank=False)
    age = models.IntegerField()
    
    