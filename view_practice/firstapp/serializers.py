
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
     name = serializers.CharField(max_length=100)
     father_name = serializers.CharField(max_length=100)
     roll_no = serializers.CharField(max_length=100)
     
