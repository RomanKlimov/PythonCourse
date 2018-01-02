from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import Message

def create_message(request):
    messages = list(Message.objects.all())
    context = {'form' : MessageForm(),
    'messages': messages}
    if request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message()
            message.text = form.cleaned_data['message_text']
            message.save()
            return redirect('/board')
        else:
            return HttpResponse("Error")
    return render(request, 'index.html', context)

def replyto(request, message_id):
    context = {'form' : MessageForm(),}
    if request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message()
            message.text = form.cleaned_data['message_text']
            message.reply_to = Message.objects.get(id = message_id)
            message.save()
            return redirect('/board#'+str(message.id))
        else:
            return HttpResponse('Error')
    return render(request, 'index.html', context)
