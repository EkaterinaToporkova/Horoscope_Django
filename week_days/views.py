from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

# def monday(request):
#     return HttpResponse('Список дел на понедельник: поехать на работу')
#
# def tuesday(request):
#     return HttpResponse('Список дел на вторник: опять поехать на работу')
day_dict = {'monday': 'Понедельник',
            'tuesday': 'Вторник',
            'wednesday': 'Среда',
            'thursday': 'Четверг',
            'friday': 'Пятница',
            'saturday': 'Суббота',
            'sunday': 'Воскресенье',
            }


def days_info(request, day: str):
    return render(request, 'week_days/greeting.html')


# noinspection PyUnreachableCode
def days_info_by_number(request, day: int):
    days = list(day_dict)
    if 1 <= day <= 7:
        name_day = days[day - 1]
        return HttpResponseRedirect(f'/todo_week/{name_day}')
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {day}')
    redirect_url = reverse('week-name', args=(name_day,))
    return HttpResponseRedirect(redirect_url)
