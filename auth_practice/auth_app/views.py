


from functools import partial
from urllib import response
from django.views import View
from .serializers import StudentSerializer, UserSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from auth_app import serializers

# Create your views here.


class StudentView(APIView):
   
    def get(self, request,):
        students = Student.objects.all()
        seria = StudentSerializer(students, many=True)
        return Response(data=seria.data)

    def post(self,request):
        data = request.data
        serial = StudentSerializer(data=data, many=False)
        if not serial.is_valid():
            return Response({'status': '403', 'error': serial.errors, 'message': 'smething went wrong'})
        elif not serial.validate:
            return Response({'status': '403', 'error': 'length short'})
            
        serial.save()
        return Response({'status': 200, 'payload': data, 'message': 'sent'})
    
    

    def patch(self, request,):
        data = request.data
        id = request.GET.get('id')
        try:    
            student = Student.objects.get(pk=id)
            serializer = StudentSerializer(student, data = data, partial=True)
            if not serializer.is_valid():
                return Response({'status': '301', 'type': 'patch', 'error': serializer.errors})
            serializer.save()
            return Response({'status': 'success', 'type': 'patch'}) 
        except Exception as e:
            return Response({'status': '301', 'type': 'patch', 'error':f'{e}' })
        
        
    """
    Delete method will delete the record base on id 
    """
    def delete(self, request):
        id = request.GET.get('id')
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return Response({'status': '200', 'type': 'put'})
        except Exception as e:
            return Response({'status':'301', 'error': f'{e}'})
    
        
    """
    Put method will update the record matching with id that is passed to it
    """
    def put(self, request,):
        
        try:
            student = Student.objects.get(pk=request.data['id'])
            data = request.data
            serializer = StudentSerializer(student, data=data)
            if not serializer.is_valid():
                return Response({'status': '301', 'type': 'put', 'error': serializer.errors})
            serializer.save()
            return Response({'status': '200', 'type': 'put'})
        except Exception as e:
            return Response({'status': '403', 'type': 'put', 'error': f'invalid id {e}'})
      
      
class UserView(APIView):
    
    def post(self, request) -> Response:
        data = request.data 
        user_serializer = UserSerializer(data=data, many=False)
        if not user_serializer.is_valid():
            return Response({'status': '401', 'error': f'{user_serializer.errors}'})
        user_serializer.save()
        
        user = User.objects.get(username=user_serializer.data['username']) 
        token , _ = Token.objects.get_or_create(user=user)
        return Response({'status': '200', 'token': str(token), 'data':user_serializer.data})
        
               
    

# @api_view(['GET'])
# def get_student(request,):
#     students = Student.objects.all()
#     seria = StudentSerializer(students, many=True)
    
#     return Response(data=seria.data)

# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     serial = StudentSerializer(data=data, many=False)
#     if not serial.is_valid():
#         return Response({'status': '403', 'error': serial.errors, 'message': 'smething went wrong'})
#     elif not serial.validate:
#         return Response({'status': '403', 'error': 'length short'})
        
#     serial.save()
#     return Response({'status': 200, 'payload': data, 'message': 'sent'})
    
    
# @api_view(['PATCH'])
# def patch_student(request,):
#     data = request.data
#     id = request.GET.get('id')
#     try:    
#         student = Student.objects.get(pk=id)
#         serializer = StudentSerializer(student, data = data, partial=True)
#         if not serializer.is_valid():
#             return Response({'status': '301', 'type': 'patch', 'error': serializer.errors})
#         serializer.save()
#         return Response({'status': 'success', 'type': 'patch'}) 
#     except Exception as e:
#         return Response({'status': '301', 'type': 'patch', 'error':f'{e}' })
    
    
# """
#   Delete method will delete the record base on id 
# """
# @api_view(['DELETE'])
# def delete_student(request):
#     id = request.GET.get('id')
#     try:
#         student = Student.objects.get(id=id)
#         student.delete()
#         return Response({'status': '200', 'type': 'put'})
#     except Exception as e:
#         return Response({'status':'301', 'error': f'{e}'})
   
    
# """
#    Put method will update the record matching with id that is passed to it
#  """   
# @api_view(['PUT'])
# def put_student(request, id):
#     try:
#         student = Student.objects.get(pk=id)
#         data = request.data
#         serializer = StudentSerializer(student, data=data)
#         if not serializer.is_valid():
#             return Response({'status': '301', 'type': 'put', 'error': serializer.errors})
#         serializer.save()
#         return Response({'status': '200', 'type': 'put'})
#     except Exception as e:
#         return Response({'status': '403', 'type': 'put', 'error': f'invalid id {e}'})
    