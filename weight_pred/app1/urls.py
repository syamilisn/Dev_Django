"""CUSTOM URLS"""
from django.urls import path
from . views import index,input,export
app_name = 'app1'

urlpatterns = [
    path('', index, name= 'index'),     #home page
    path('input/',input, name = 'input'),   #user input page
    path('export/', export , name= 'export'), #HomePage

]