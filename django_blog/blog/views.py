from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer, CommentCreateSerializer


class CreatePost(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentCreateViewSet(ModelViewSet):
    serializer_class = CommentCreateSerializer
