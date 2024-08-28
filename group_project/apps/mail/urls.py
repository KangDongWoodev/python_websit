# apps/mail/urls.py

from django.urls import path
from . import views

app_name = 'mail'

urlpatterns = [
    path('', views.mail_list, name='mail_list'),
    path('compose/', views.send_mail, name='compose_mail'),
    path('<int:mail_id>/', views.mail_detail, name='mail_detail'),
]