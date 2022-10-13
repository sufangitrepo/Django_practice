
from blogers.models import AuthorModel
from rest_framework import serializers

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    

class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    author = serializers.CharField(max_length=500)
    title = serializers.CharField(max_length=500)
    tagline = serializers.CharField(max_length=300)
    

class EntrySerializer(serializers.Serializer):
    detail= serializers.CharField(max_length=2000)
    blog_id = serializers.CharField(max_length=500)
    rating = serializers.CharField(max_length=20)
    published_date = serializers.DateField()             