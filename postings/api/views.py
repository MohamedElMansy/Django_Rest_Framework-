from rest_framework import generics
from postings.models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BasicAuthentication

class BlogPostRUDView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field='id'
    serializer_class = BlogPostSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
    def get_queryset(self):
        return BlogPost.objects.all()

class BlogPostapiView(generics.ListAPIView):

    lookup_field='id'
    serializer_class = BlogPostSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
    def get_queryset(self):
        return BlogPost.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
