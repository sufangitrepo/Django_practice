

from django.urls import path
from fristapp import views

urlpatterns = [
    path(route='home/<int:a>', view=views.home, name='home')
]