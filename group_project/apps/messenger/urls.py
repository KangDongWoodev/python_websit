# apps/messenger/urls.py

from django.urls import path
from . import views

app_name = 'messenger'

urlpatterns = [
    path('chat/', views.chat_list_view, name='chat_list'),  # 추가된 URL 패턴
    path('chat/<str:room_name>/', views.chat_room_view, name='chat_room'),
]