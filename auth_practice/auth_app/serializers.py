
from dataclasses import fields
from pyexpat import model
from statistics import mode
from unicodedata import category
from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User
class StudentSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Student
        fields = '__all__'
        
    def validate(self, data):
        
        if len(data['name']) <= 10:
            raise serializers.ValidationError({'error': 'name length should >= 10'})     
        
        return data
        
        


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        
        
        
        
# class MySerializer(serializers.ModelSrializer):
    
#     class Meta:
#         model = Student
#         # fields = ['', '', '',...]  all fields that shoud be parse
#         # fields = '__all__'         all fields avaiable in model
#         # exclude = ['']             all fields except the mentions here 
"""
 Nested Serializer with foriegn key
"""        

# class Outer(serializers.ModelSrializer):
    
#     category = Student()
#     class Meta:
#         model = Student
#         fields = '__all__'        
    
