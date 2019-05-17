

from django.contrib import admin
from django.urls import path
from .views import BlogPostRUDView


urlpatterns = [
    path('<int:id>', BlogPostRUDView.as_view())
]
