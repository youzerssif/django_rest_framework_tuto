from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

# Create your views here.

class PostList(generics.ListCreateAPIVIEW):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass

class PostDetail(generics.RetrieveDestroyAPIVIEW):
    pass

