from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def home(request, a) -> HttpResponse:
    return HttpResponse('hello world')