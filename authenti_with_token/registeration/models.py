

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
    )
from django.db import models



#Create USerManager here
class UserManager(BaseUserManager):
    
    
    def show(self):
        print('Show$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ShowWW')
    def create_user(self, username, email, password=None , **extra_fields):
        if email is None:
            raise TypeError('email should be given')
        elif username is None:
            raise TypeError('username should be given')
        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        print('######################################################################')
        user.save()
        return user
    def create_superuser(self, username, email, password=None, **extra_fields):
        if password is None:
            raise TypeError('password should be given')
        user = self.create_user(username=username,email=email,password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

# Create your models here.


class UserModel(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(unique=True, db_index=True)
    username = models.CharField(max_length=255, db_index=True)
    is_verified = models.BooleanField(default=False,)
    is_active = models.BooleanField(default=True,)
    is_staff  = models.BooleanField(default=False,)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
    objects = UserManager()
    
    
    def __str__(self):
        return self.email
    
    
    def token(self):
        return ''
    
    
    






class StudentManager(models.Manager):
    def show(self):
        print('show')
   
    



class StudentModel(models.Model):
    
    name = models.CharField(max_length=255)
    id = models.AutoField(auto_created=True, primary_key=True)
    age = models.PositiveIntegerField(blank=False)
    semester = models.CharField(max_length=255, blank=False)
    
    
    objects = StudentManager()
    