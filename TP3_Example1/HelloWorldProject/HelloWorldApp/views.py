from django.shortcuts import render
from django.http import HttpResponse

def hello_world_html(request):
    return render(request, 'hello_world_html.html')

def hello_world(request):
    return HttpResponse('Hello World ! Baptiste CUIGNEZ   ---    add [/hello_world_html] at the end of this URL to find Hello World with a little bit of CSS')


