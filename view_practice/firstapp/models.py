from django.db import models

class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    