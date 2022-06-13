
from csv import excel
import json
import requests # pip install requests
from multiprocessing import context
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import models
from django.urls import reverse # для перекидывание страницы reverse
from . import utils #пагинатор




def index (request):
    context = {

    }
    return render(request, 'pages/home.html', context) 


def mylist (request):
    tasks = models.Task.objects.all()

    count_object_on_one_page = 2
    curent_page_from_request_parametr = request.GET.get('page')
    pages_obj = utils.CustomPaginator.get_page(
        objs=tasks,
        limit =count_object_on_one_page,
        current_page=curent_page_from_request_parametr
    )
    context = {
        "page": pages_obj
    }  
    # context= {
    #     "tasks": tasks 

    # }
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

def update_todolist_status(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)

    if obj.is_completed:
        obj.is_completed = False
    else:
        obj.is_completed = True
    obj.save()
    return redirect(reverse('mylist', args=()))

def delete_todolist(request, todo_id):
    obj = models.Task.objects.get(id=todo_id)
    obj.delete()
    return redirect(reverse('mylist', args=()))

def get_vacancies(request):
    context = {

    }
    if request.method == "POST":
        vacancie = request.POST.get("vacancie", "Никто")
        
        params = {
            'text': f'NAME:{vacancie}',
            'area': 40,
            'page': 1,
            'per_page': 100
        }

        response = requests.get('https://api.hh.ru/vacancies', params)
        json_data1 = json.loads(response.content.decode())

        vacancies = json_data1["items"]

        # for i in vacancies:
        #     print(i)
        #     print("\n\n")
        
        # print(f'длина: {len(vacancies)}')


        

        context ={
            "vacancie": vacancie,
            "vacancies": vacancies
        }
    return render(request, 'pages/vacanciespage.html', context)