from email import message
from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.
from chat.models import ChatModel
User=get_user_model()

def index(request):
    users=User.objects.exclude(username=request.user.username)
    return render(request, 'index.html',context={'users':users})

def chatPage(request,username):
    user_obj=User.objects.get(username=username)
    users=User.objects.exclude(username=request.user.username)

    if request.user.id>user_obj.id:
        thread_name=f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name=f'chat_{user_obj.id}-{request.user.id}'

    message_obj=ChatModel.objects.filter(thread_name=thread_name)
    return render(request, 'main_chat.html',context={
        'users':users,
        'user':user_obj,
        'messages':message_obj,
        })