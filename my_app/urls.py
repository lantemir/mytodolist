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
]
