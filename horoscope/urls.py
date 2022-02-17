from django.urls import path, register_converter
from . import views as views_horoscope, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')


urlpatterns = [
    path('', views_horoscope.index, name='horoscope-index'),
    path('<yyyy:sign_zodiac>/', views_horoscope.get_yyyy_converters),
    path('<int:month>/<int:day>/', views_horoscope.get_info_by_date),
    path('type/', views_horoscope.get_type),
    path('<int:sign_zodiac>/', views_horoscope.get_info_about_sign_zodiac_by_number),
    path('<my_float:sign_zodiac>/', views_horoscope.get_my_float_converters),
    path('<str:sign_zodiac>/', views_horoscope.get_info_about_sign_zodiac, name='horoscope-name'),
    path('type/<str:sign>/', views_horoscope.get_type_sign, name='type-name'),
    path('<my_date:sign_zodiac>', views_horoscope.get_my_date_converters),
]
