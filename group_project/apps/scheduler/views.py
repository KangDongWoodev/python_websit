# apps/scheduler/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'scheduler/home.html')  # 템플릿 파일을 렌더링