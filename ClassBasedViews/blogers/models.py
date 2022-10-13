
from django.db import models

# Create your models here.

class AuthorModel(models.Model):
    id = models.IntegerField(primary_key=True,)
    name = models.CharField(max_length=50)
    email = models.EmailField(null=False, blank=False,  )
    
    
    
class BlogModel(models.Model):
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    tagline = models.CharField(max_length=300)
    

class EntryModel(models.Model):
    detail= models.TextField()
    blog_id = models.OneToOneField(BlogModel, on_delete=models.CASCADE)
    # models.ForeignKey(BlogModel, on_delete=models.CASCADE, unique=True)
    rating = models.CharField(max_length=20)
    published_date = models.DateField() 
           
        