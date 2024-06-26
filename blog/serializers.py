from .models import Blog, BlogUser
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class BlogSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Blog
		fields = ['id', 'title', 'body']

class BlogUserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = BlogUser
		fields = ['id', 'first_name', 'last_name']