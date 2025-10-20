"""CUSTOM URLS"""
from django.urls import path
from . views import index, input, edit
app_name = 'app1'
urlpatterns = [
    #index page
    path('',index, name = 'index'),
    #user input page
    path('input/',input, name = 'input'),
    #edit user input page
    path('edit/<int:intro_id>/', edit, name ='edit'),
]