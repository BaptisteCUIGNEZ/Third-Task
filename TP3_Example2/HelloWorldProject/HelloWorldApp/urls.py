# urls.py
from django.urls import path
from .views import message_list, add_message

urlpatterns = [
    path('', message_list, name='message_list'),
    path('add/', add_message, name='add_message'),
]

