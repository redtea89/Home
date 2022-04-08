from rest_framework import serializers
from exercise.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'
    
    def create(self, validated_data):
        return Exercise.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)
        return instance





