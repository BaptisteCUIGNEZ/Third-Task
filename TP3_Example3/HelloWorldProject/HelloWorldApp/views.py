
from django.shortcuts import render
from .models import Message

def hello_world_html(request):
    return render(request, 'hello_world.html')

def messages_home(request):
    return render(request, 'messages/messages_home.html')

def submit_message(request):
    if request.method == 'POST':
        sender = request.POST['sender']
        recipient = request.POST['recipient']
        content = request.POST['content']

        Message.objects.create(sender=sender, recipient=recipient, content=content)

        return render(request, 'messages/submit_success.html')

    return render(request, 'messages/submit_message.html')


def get_messages(request):
    if request.method == 'POST':
        recipient = request.POST['recipient']
        messages = Message.objects.filter(recipient=recipient).order_by('-timestamp')[:3]
        return render(request, 'messages/message_list.html', {'messages': messages})

    return render(request, 'messages/get_messages.html')


