from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskList(APIView):
    def get(self,request,*args,**kwargs):
        tasks = Task.objects.all()
        tasks = TaskSerializer(tasks,many=True)
        return Response(tasks.data)
    
    def post(self,request,*args,**kwargs):
        newTask = TaskSerializer(data=self.request.data)
        if newTask.is_valid():
            newTask.save()
        return Response(newTask.data)
    
class TaskDetail(APIView):
    def get(self,request,*args,**kwargs):
        task = Task.objects.get(id=self.kwargs['pk'])
        task = TaskSerializer(task)
        return Response(task.data)
    
    def post(self,request,*args,**kwargs):
        task = Task.objects.get(id=self.kwargs['pk'])
        task = TaskSerializer(instance=task, data=self.request.data)
        if task.is_valid():
            task.save()
        return Response(task.data)
    
    def delete(self,request,*args,**kwargs):
        Task.objects.get(id=self.kwargs['pk']).delete()
        return Response('Item succsesfully delete!')
    
