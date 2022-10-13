
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.StudentView.as_view(),),
    path('register/', views.UserView.as_view())
    # path('add/', views.post_student),
    # path('change/<int:id>', views.put_student),
    # path('p_change/', views.patch_student),
    # path('remove/', views.delete_student),
    
    
]
