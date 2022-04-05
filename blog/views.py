from django.shortcuts import render
from rest_framework import viewsets, permissions
from blog.serializers import BlogSerializer
from blog.models import Blog

# Create your views here.
def index(request):
    writing4 = Blog.objects.all().order_by('-created')[1:5]
    writing8 = Blog.objects.all().order_by('-created')[5:9]
    writing12 = Blog.objects.all().order_by('-created')[9:13]
    writing = Blog.objects.all()
    writingLast = Blog.objects.last()
    return render(request, 'index.html',{'number':range(4),
    'writing':writing,'writing4':writing4,
    'writingLast':writingLast, 'writing':writingLast, 'writing8':writing8,
    'writing12':writing12})

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created')
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

def blog(request, textId):
    writing = Blog.objects.get(id=textId)
    return render(request, 'blog/blog.html',{'writing':writing})