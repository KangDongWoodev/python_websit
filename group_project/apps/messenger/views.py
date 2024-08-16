# apps/messenger/views.py

from django.shortcuts import render

def chat_list_view(request):
    return render(request, 'messenger/chat_list.html')

def chat_room_view(request, room_name):
    return render(request, 'messenger/chat_room.html', {
        'room_name': room_name
    })