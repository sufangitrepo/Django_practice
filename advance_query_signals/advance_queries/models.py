from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return 'category: {}, id: {}'.format(self.name, self.id)


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_id')

       
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    size = models.CharField(max_length=300)
    information = models.TextField()
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)         