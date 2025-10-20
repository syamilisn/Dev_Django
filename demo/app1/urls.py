"""CUSTOMS"""
from django.urls import path
from .views import current_datetime, index, upload_file,export
app_name = 'app1'
urlpatterns = [
    path('', export , name= 'export'), #HomePage
    path('index/', index , name= 'index'), #HomePage
    path('current_datetime/', current_datetime , name= 'current_datetime'), #date time page
    path('upload_file/', upload_file , name= 'upload_file'), #upload file in form
]