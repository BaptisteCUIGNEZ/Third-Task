
from django.urls import path
from .views import *

urlpatterns = [
    path('messages/submit/', submit_message, name='submit_message'),
    path('messages/get/', get_messages, name='get_messages'),
    path('messages/', messages_home, name='messages_home'),
    path('', hello_world_html, name='hello_world_html')
]
