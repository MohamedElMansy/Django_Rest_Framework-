

from django.contrib import admin
from django.urls import path
from .views import BlogPostRUDView ,BlogPostapiView


urlpatterns = [
    path('', BlogPostapiView.as_view()),
    path('<int:id>', BlogPostRUDView.as_view())
]
