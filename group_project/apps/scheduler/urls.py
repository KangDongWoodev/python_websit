from django.urls import path
from . import views

app_name = 'scheduler'

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/new/', views.event_create, name='event_create'),
    path('<int:year>/<int:month>/', views.calendar_view, name='calendar_by_month'),
]