# views.py
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

def message_list(request):
    messages = Message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})

def add_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_list')
    else:
        form = MessageForm()

    return render(request, 'add_message.html', {'form': form})




