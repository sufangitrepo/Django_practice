



from django.urls import path
from .views import DefaultApiView



urlpatterns = [
    path('', DefaultApiView.as_view())
]
