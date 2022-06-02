
from asyncio import tasks
from multiprocessing import context
from turtle import title
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from . import models



def index (request):
    context = {

    }
    return render(request, 'pages/home.html', context) 


def mylist (request):
    tasks = models.Task.objects.all()

  
    context= {
        "tasks": tasks 

    }
    return render(request, 'pages/mylist.html', context)

def createtodo (request):
    if request.method == "POST":
        titleadd = request.POST.get("title", "заголовок по умолчанию")
        descriptionadd = request.POST.get("description", "описание по умолчанию")
        obj = models.Task.objects.create(
            title= titleadd,
            description=descriptionadd
        ) 
        obj.save()
    context ={

    }
    return render(request, 'pages/createlist.html', context)

def updatetodo (request, todo_id):
    obj = models.Task.objects.get(id = todo_id)

    if request.method == "POST":
        title1 = request.POST.get("title", "заголовок по умолчанию")
        description1 = request.POST.get("description", "описание по умолчанию")
        if obj.title != title1:
            obj.title = title1
        if obj.description != description1:
            obj.description = description1
        obj.save()
    context = {
        "todo" : obj
    }
    return render(request, 'pages/updatelist.html', context)

def detailtodo (request, todo_id):
    obj = models.Task.objects.get(id = todo_id)
    context = {
        "todo": obj
    }
    return render(request, 'pages/detaillist.html', context)

def home (request):
    context = {

    }
    return render(request, 'pages/home.html', context)