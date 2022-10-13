from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Employ(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    emp_id = models.IntegerField()
    emp_salary = models.DecimalField(decimal_places=2, max_digits=20)
    