

from django.urls import path
from .views import AuthorView, BlogView

urlpatterns = [
  # Author routes
  path('author/', AuthorView.as_view(), ),
  path('author/<int:id>/', AuthorView.as_view()),
  
  # Blog routes
  path('author/<int:author_id>/blogs/', BlogView.as_view()),
  path('blog/<int:blog_id>/', BlogView.as_view()),
  
 
  
      
]


