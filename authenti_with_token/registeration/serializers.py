


from .models import UserModel
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = '__all__'
    
        