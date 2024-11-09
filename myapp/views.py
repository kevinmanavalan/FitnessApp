# from django.http import JsonResponse
from rest_framework import viewsets, permissions
from .serializer import ExerciseSerializer
from .models import Exercises
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

# class ExerciseViewSet(viewsets.ModelViewSet):
#     queryset = Exercises.objects.all().order_by('id')
#     serializer_class = ExerciseSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# def getExercises(request):
#     exercises = Exercises.objects.all()
#     dict_exercises = list(exercises.values())
#     return JsonResponse(dict_exercises, safe=False)

@api_view(['GET'])
def getExercises(request):
    exercises = Exercises.objects.all()
    serializer = ExerciseSerializer(exercises, many = True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def add_Exercise(request):
    serializer = ExerciseSerializer(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
