

from django.urls import path
from .views import EmployView

urlpatterns = [
    path('employ/', EmployView.as_view())
]
