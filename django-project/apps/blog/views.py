from django.http import HttpResponse

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Post, Comment
from .serializers import *

def index(request):
    url = "https://github.com/users/redtea89/projects/2/views/1"
    repo = "https://github.com/redtea89/Home"
    return HttpResponse(f"<h1>[공사중...3] 홈페이지 리뉴얼중입니다.</h1><h4><a href={url}>프로젝트 진행과정 확인하기</a></h4><h4><a href={repo}>레포지터리</a></h4>")


class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all().order_by('-updated_at')
    serializer_class = PostListSerializer


class PostRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer