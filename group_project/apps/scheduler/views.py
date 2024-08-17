from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Event
from .forms import EventForm  # Assuming you have a form class for Event
import calendar

def calendar_view(request, year=None, month=None):
    today = timezone.now()
    
    # 현재 연도와 월을 기본값으로 설정
    if year is None:
        year = today.year
    if month is None:
        month = today.month

    # 유효한 연도와 월인지 확인
    try:
        year = int(year)
        month = int(month)
        if month < 1 or month > 12:
            raise ValueError
    except (ValueError, TypeError):
        return HttpResponse("잘못된 연도나 월입니다.", status=400)

    # 달력 생성
    cal = calendar.Calendar(firstweekday=0)
    month_days = cal.monthdayscalendar(year, month)

    # 해당 달의 모든 이벤트를 가져옵니다
    events = Event.objects.filter(start_date__year=year, start_date__month=month)

    # 날짜별 이벤트를 매핑
    days = {day: [] for day in range(1, 32)}  # 최대 31일을 기본값으로 설정
    for event in events:
        day = event.start_date.day
        days[day].append(event)

    # 달력의 각 주와 그에 포함된 일들을 나타내기 위한 구조
    calendar_weeks = []
    for week in month_days:
        week_days = []
        for day in week:
            if day == 0:
                week_days.append({
                    'day': None,
                    'events': []
                })
            else:
                week_days.append({
                    'day': day,
                    'events': days.get(day, [])
                })
        calendar_weeks.append(week_days)

    # 템플릿에 필요한 데이터를 전달합니다
    context = {
        'year': year,
        'month': month,
        'calendar_weeks': calendar_weeks,
        'year_range': range(today.year - 5, today.year + 6),  # 예: 5년 전부터 5년 후까지의 범위
        'month_range': range(1, 13),  # 1월부터 12월까지
    }

    return render(request, 'scheduler/calendar.html', context)

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    context = {
        'event': event,
    }
    return render(request, 'scheduler/event_detail.html', context)

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scheduler:calendar')  # Redirect to calendar view after saving
    else:
        form = EventForm()

    context = {
        'form': form,
    }
    return render(request, 'scheduler/event_form.html', context)