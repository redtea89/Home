from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ['title','subtitle','text','tag','created','updated']