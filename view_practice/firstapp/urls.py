
from django.urls import path

from firstapp.views import HomeViewGet

urlpatterns = [
    path(route='', view= HomeViewGet.as_view(), name='get'),
    
    
]