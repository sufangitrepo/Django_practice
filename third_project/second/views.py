from cgitb import reset
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request, a,b) -> HttpResponse:
    return HttpResponse(f'sum is = {a+b}  jhj')

def home(request) -> HttpResponse:
    return HttpResponse(f'{request}')
    