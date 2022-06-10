from django.http import HttpResponse

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Post, Comment
from .serializers import *


class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer