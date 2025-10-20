"""CUSTOM URLS"""
from django.urls import path
from . views import index, topics, topic
app_name = 'app1'

urlpatterns = [
    path('', index, name= 'index'),     #home page
    path('topics/', topics, name= 'topics'),     #topics list page
    path('topics/<int:topic_id>', topic, name = 'topic'),
]