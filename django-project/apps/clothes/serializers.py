from rest_framework import serializers

from .models import Clothes, History


class ClothesListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Clothes
        fields = '__all__'


class ClothesDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Clothes
        fields = '__all__'
        read_only_fields = ['id', 'updated_at',]
