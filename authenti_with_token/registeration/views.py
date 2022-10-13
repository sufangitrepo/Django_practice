import imp
from .serializers import RegisterSerializer
from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your views here.

@api_view(['GET'])
def login(request, email, password):
    try:
        user = User.objects.get(email=email)
        user_ser = RegisterSerializer(user, many=False)
        token = Token.objects.get(user_id=user_ser['id'])
        return Response({'status':200, 'payload': str(token)})
    except Exception as  e:
        return Response({'status':401, 'error': f'{e}'}) 




class RegisterView(views.APIView):
    
    
    def get(self, request):
        pass
    
    def post(self, request):
        req_body = request.data 
        serialize = RegisterSerializer(data=req_body)
        if not serialize.is_valid():
            return Response({'status': 403, 'error': serialize.errors})
       
        print("##########################################")
        # serialize.create()
        
        print(model = serialize)
        serialize.save()
        
        User = get_user_model()
        user = User.objects.get(email=serialize.data['email']) 
        token , _  = Token.objects.get_or_create(user=user)
        return Response({'status': 200, 'token': str(token)})
           
    