from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def get_rectangle_area(request, width: int, height: int):
    return render(request, 'geometry/rectangle.html')
    #return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def get_square_area(request, width: int):
    return render(request, 'geometry/square.html')
    #return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width ** 2}')


def get_circle_area(request, radius: int):
    return render(request, 'geometry/circle.html')
    #return HttpResponse(f'Площадь круга радиусом {radius} равна {radius ** 2}')


def func_rectangle(request, width: int, height: int):
    s = width * height
    redirect_url = reverse('rectangle', args=(width, height, ))
    return HttpResponseRedirect(redirect_url)


def func_square(request, width: int):
    s = width ** 2
    redirect_url = reverse('square', args=(width, ))
    return HttpResponseRedirect(redirect_url)


def func_circle(request, radius: int):
    s = 3.14 * (radius ** 2)
    redirect_url = reverse('circle', args=(radius, ))
    return HttpResponseRedirect(redirect_url)
