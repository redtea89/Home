from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

import tweepy
from local_settings import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

from .models import Clothes, History
from .serializers import *

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

# api.update_status("Hello Tweepy")

class SuggetionView(APIView):
    def get(self, request):
        queryset = History.objects.all()

        # 지난 기록 10개
        objs = queryset.filter(wearing=1)[:10]

        # 10개를 기준으로 현재입을 옷 추천
        '''
        옷 고르는 구현함수 지점
        '''

        # 추천 메시지
        return Response({"message": "오늘은 흰색 상의, 청색 바지를 입으세요."})


class ClothesListCreateView(ListCreateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesListSerializer


class ClothesRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesDetailSerializer