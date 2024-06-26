from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

class BlogUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)