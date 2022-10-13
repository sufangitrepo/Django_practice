from account.models import UserModel
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework.response import Response


#HTTP 401 Unauthorized
#HTTP 403 Permission Denied

#function based view
@api_view(['POST'])
def login(request):
    body = request.data
    try:
        user = UserModel.objects.get(email=body['email'])
        token = Token.objects.get(user_id=user.id)
        return Response({'status':200, 'token': str(token)})
    
    except Exception as e:
        return Response({'status':401, 'error':str(e)})
    

#class based view




class RegisterUserView(APIView,):
    
    def post(self, request):
        body = request.data
        serializer = UserSerializer(data=body)
        
        if not serializer.is_valid():
            return Response({'status': 200, 'error': serializer.errors})
        serializer.save()
        user = UserModel.objects.get(email=serializer.data['email'])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'status': 200, 'token': str(token)})
    

