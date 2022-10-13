"""
  This module have view of first app
"""
import imp
import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from firstapp.models import StudentModel
from firstapp.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

def about(request):
  return 

class HomeViewGet(View):
    """
      HomePAgeGet class is a view for Get Request  
    """
    
    def get(self, request,):
        st = StudentModel.objects.all()
        serializer = StudentSerializer(st,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return  HttpResponse(json_data,)
    
 
    