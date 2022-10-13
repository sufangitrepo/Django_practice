
from django.http import JsonResponse

def home(request):
    return JsonResponse({'data':'home page of this project'}, safe=False)