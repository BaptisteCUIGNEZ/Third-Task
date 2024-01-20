from django.urls import path
from .views import *

urlpatterns = [
    
    path('', hello_world, name='hello_world'),
    path('hello_world_html/', hello_world_html, name='hello_world_html'),
]