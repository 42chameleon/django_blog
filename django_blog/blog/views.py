from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer


class CreatePost(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
