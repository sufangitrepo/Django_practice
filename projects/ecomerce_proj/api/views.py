
from rest_framework.views import APIView
from rest_framework.response import Response


class DefaultApiView(APIView):
    
    
    def get(self, request):
        return Response({'result': 'api view get'})
