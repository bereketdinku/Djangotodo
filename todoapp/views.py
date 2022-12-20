from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import todolist
from .serializer import todoSerializer
# Create your views here.
@api_view(['GET'])
def taskview(request):
    task=todolist.objects.all()
    serializer=todoSerializer(task,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def taskDetail(request,pk):
    task=todolist.objects.get(id=pk)
    serializer=todoSerializer(task,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def createtask(request):
    serializer=todoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def taskupdate(request,pk):
    task=todolist.objects.get(id=pk)
    serializer=todoSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def taskDelete(request,pk):
    task=todolist.objects.get(id=pk)
    task.delete()