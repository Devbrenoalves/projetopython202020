from django.shortcuts import render
from django.contrib import messages

def inbox(request):

    return render(request, "chat/main/messenger.html")
