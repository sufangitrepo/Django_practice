
from dataclasses import dataclass
from functools import partial
import re
from .serializers import EmpSerializer
from .models import EmployModel
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view([''])
def show(request):
    pass


class EmployView(APIView):
    
    def get(self, request):
        employs = EmployModel.objects.all()    
        parsed_employ = EmpSerializer(employs, context={}, many=True, partial=False)
        return Response(parsed_employ.data)
    
    def post(self, request):
        request_body = request.data
        try:
            serialized = EmpSerializer(data=request_body, context={}, many=False, partial=False)
            if not serialized.is_valid():
                return Response({'status': '403', 'error':serialized.errors})
            serialized.save()
            return Response({'status': '200', 'payloads':serialized.data})
        except Exception as e:
            return Response({'status': '403', 'error':f'{e}'})
    
    
    def put(self, request,):
        id = request.GET.get('id')
        try:
            body = request.data
            query = EmployModel.objects.get(id = id)
            serializer = EmpSerializer(query, data=body, partial=False, context={})
            if not serializer.is_valid():
                return Response({'status':403, 'error': serializer.errors})
            serializer.save()
            return Response({'status':200, 'payload':serializer.data})
        except Exception as e:
            return Response({'status':403, 'error': f'{e}'})


    def delete(self, request):
        id = request.GET.get('id')
        try:
            emp = EmployModel.objects.get(id=id)            
            emp.delete()
            return Response({'status':200, 'id': id})    
        except Exception as e:
            return Response({'status':403, 'error': f'{e}'})    
        
        
    def patch(self, request):
        id = request.GET.get('id')    
        body = request.data 
        try:
            emp = EmployModel.objects.get(id=id)    
            serializer = EmpSerializer(emp,data=body,partial=True)
            if not serializer.is_valid():
                return Response({'status':403, 'error': serializer.errors})
            serializer.save()
            return Response({'status':200, 'payload': serializer.data})     
        except e:
            return Response({'status':403, 'error': f'{e}'})