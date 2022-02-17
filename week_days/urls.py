from django.urls import path
from week_days import views as views_week

urlpatterns = [
    path('<int:day>/', views_week.days_info_by_number),
    path('<str:day>/', views_week.days_info, name='week-name')
]
