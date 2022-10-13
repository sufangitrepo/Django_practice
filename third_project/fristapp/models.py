
from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=50)
    detail_info = models.TextField()
