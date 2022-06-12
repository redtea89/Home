from django.http import HttpResponse

import logging

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Post, Comment
from .serializers import *


class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def get(self, request, *args, **kwargs):
        logging.basicConfig(
            filename='example.log',
            format='%(asctime)s %(message)s',
            encoding='utf-8',
            level=logging.DEBUG)
        logging.info('posts [GET]')
        return self.list(request, *args, **kwargs)


class PostRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer