from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass

# Create your views here.

zodiac_dict = {
    'aries': ('Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).', 81, 111),
    'taurus': ('Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).', 112, 142),
    'gemini': ('Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).', 143, 173),
    'cancer': ('Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).', 174, 204),
    'leo': ('Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).', 205, 234),
    'virgo': ('Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).', 235, 267),
    'libra': ('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).', 268, 297),
    'scorpio': ('Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).', 298, 327),
    'sagittarius': ('Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).', 328, 357),
    'capricorn': ('Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).', 358, 366),
    # с 23.12 по 31.12
    'Сapricorn': ('Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).', 1, 20),
    # с 31.12 по 20.01
    'aquarius': ('Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)', 21, 50),
    'pisces': ('Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).', 51, 80),
}

type_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}

day_month = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число из 4 цифр - {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число - {sign_zodiac}')


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату - {sign_zodiac}')


def index(request):
    zodiacs = list(zodiac_dict)
    del zodiacs[10]
    # f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    context = {
        'zodiacs': zodiacs,
    }
    return render(request, 'horoscope/index.html', context=context)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    zodiacs = list(zodiac_dict)
    del zodiacs[10]
    if description:
        data = {
            'description_zodiac': description[0],
            'sign': sign_zodiac,
            'sign_name': description[0].split()[0],
            'zodiacs': zodiacs,
        }
    else:
        data = {
            'description_zodiac': description,
            'sign': sign_zodiac,
        }

    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs) or sign_zodiac <= 0:
        return HttpResponseNotFound(f'Неправильный номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def get_type(request):
    li_elem = ''
    for elem in list(type_dict):
        redirect_type = reverse('type-name', args=[elem])
        li_elem += f"<a href='{redirect_type}'><li>{elem.title()} </li> </a>"
    return HttpResponse(f"<ul>{li_elem}</ul>")


def get_type_sign(request, sign: str):
    li_elem = 'Нет такой стихии'
    if sign in type_dict:
        li_elem = ''
        for st in type_dict[sign]:
            sign_url = reverse('horoscope-name', args=[st])
            li_elem += f"<a href='{sign_url}'><li>{st.title()}</a></li>"
    return HttpResponse(f"<ul>{li_elem}</ul>")


def get_info_by_date(request, month: int, day: int):
    day_num_list = []
    for i in range(1, month):
        day_num_list.append(day_month[i])
    day_num = sum(day_num_list) + day
    for sign in zodiac_dict:
        if zodiac_dict[sign][1] <= day_num <= zodiac_dict[sign][2]:
            redirect_url = reverse('horoscope-name', args=(sign,))
            return HttpResponseRedirect(redirect_url)
