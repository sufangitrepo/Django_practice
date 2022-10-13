


from django.urls import path
from  .views import RegisterUserView, login

urlpatterns = [
                 
    path('register/', RegisterUserView.as_view()),
    path('login/', login)
    
]