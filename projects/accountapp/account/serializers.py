
from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from account.models import UserModel


class UserSerializer(ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = '__all__'
        
        
        


