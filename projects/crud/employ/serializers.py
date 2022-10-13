


from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import EmployModel


class EmpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmployModel
        fields = '__all__'
        validator = []
        
    
    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError('age should be >= 18')
        return age
    
    def validate_salary(self, u):
        if u < 0:
           raise serializers.ValidationError('salary should be positive')
        return u

        
        