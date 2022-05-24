from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

def index(request):
    return HttpResponse("<h1>[공사중...2] 홈페이지 리뉴얼중입니다.</h1>")


class IndexListView(ListView):
    pass


class IndexDetailView(DetailView):
    pass