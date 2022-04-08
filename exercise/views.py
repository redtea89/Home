from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from exercise.models import Exercise
from exercise.serializers import ExerciseSerializer
from django.http import Http404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class ExerciseView(generic.View):
    def get(self,request):
        data = Exercise.objects.all()
        context = {'data':data}
        return render(request, 'exercise/exercise.html',context)


@api_view(['GET','POST'])
@csrf_exempt
def exercise_list(request):
    if request.method == 'GET':
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
        # return JsonResponse(serializer.data, safe=False)
    
    # elif request.method == 'POST':
    #     serializer = ExerciseSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExerciseSerializer(data = data)
        if serializer.is_valid():
            #serializer.save()함수는 serializer.py의 여러 함수들에 해당함. (중요)
            serializer.save()
            # return Response(serializer.data)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

# @api_view(['GET','PUT','DELETE'])
# @csrf_exempt
# def exercise_detail(request,pk):
#     try:
#         exercise = Exercise.objects.get(pk=pk)
#     except Exercise.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ExerciseSerializer(exercise)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ExerciseSerializer(exercise, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         exercise.delete()
#         return HttpResponse(status=204)

    