from django.http import HttpResponse

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Post, Comment
from .serializers import *

def index(request):
    return HttpResponse("<h1>[공사중...2] 홈페이지 리뉴얼중입니다.</h1>")


class PostListCreatetView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer