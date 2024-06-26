from django.shortcuts import render

from .models import Blog, BlogUser
from rest_framework import viewsets, permissions
from .serializers import BlogSerializer, BlogUserSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permissions_class = [permissions.AllowAny]


class BlogUserViewSet(viewsets.ModelViewSet):
    queryset = BlogUser.objects.all()
    serializer_class = BlogUserSerializer
    permissions_class = [permissions.AllowAny]
