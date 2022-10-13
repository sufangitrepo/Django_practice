

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from rest_framework.authtoken.models import Token


# Create your models here.
class UserManager(BaseUserManager):
    
    
    def create_user(self, email: str, username: str, password=None,
                    **extra_fields
                    ):
        """
         this method will create new user in database
         and return that newly created user
         params:

            email       email of newly created user
            phone       phone number of newly created user
            username    username of user
            password    password for user
            
        these are mandatory fields for every user
        there are some other fields that will be default if 
        not given    
        """
        if username is None:
            raise TypeError('username should not be null')
        elif email is None:
            raise TypeError('email should not be null')
        elif password is None:
            raise TypeError('password should not be null')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
   
   
    def create_superuser(self, email, username, password, **extra_fields):
        """
        this method will create superuser and will return that user
        Params
        
            email            email of user
            phone            phone number of user  
            username         username   
            password         password for user
            is_superuser     this fileld will be true 
            is_staff         it also will be true 
            
        remaiinig other fields are set to be default if not given     
        """
        if password is None:
             raise TypeError('password should not be null')
        user = self.create_user(email=email, password=password, 
                                username=username,  
                                **extra_fields)
        print('#######################################################3')
        user.is_superuser = True
        user.is_staff = True 
        user.save()
        return user
    
    
    
class UserModel(AbstractBaseUser, PermissionsMixin):
    
    
    username = models.CharField(max_length=255, blank=True, unique=False, null=False)
    password = models.CharField(max_length=255, blank=False, unique=False, null=False)        
    email = models.EmailField(unique=True, blank=False, null=False)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 
    
    objects = UserManager()
    
    
    def __str__(self):
        return self.email