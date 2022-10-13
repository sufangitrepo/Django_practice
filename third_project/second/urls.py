
from django.urls import path
from second import views

urlpatterns = [
    path(route='about/<int:a>,<int:b>', view=views.about, name='about'),
    path(route='', view=views.home, name="home")
    
]
