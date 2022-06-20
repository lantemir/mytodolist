from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('mylist/', views.mylist, name="mylist"),
    path('createtodo/', views.createtodo, name="createtodo"),
    path('updatetodo/<int:todo_id>/', views.updatetodo, name="updatetodo"),
    path('detailtodo/<int:todo_id>/', views.detailtodo, name="detailtodo"),
    path('update_todolist_status/<int:todo_id>/', views.update_todolist_status, name="update_todolist_status"),
    path('delete_todolist/<int:todo_id>/', views.delete_todolist, name="delete_todolist"),
    path('get_vacancies/', views.get_vacancies, name="get_vacancies"),
    path('dollar_parser/', views.dollar_parser, name="dollar_parser"),
]
