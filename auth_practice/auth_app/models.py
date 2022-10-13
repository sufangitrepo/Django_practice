from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    f_name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(default=18)