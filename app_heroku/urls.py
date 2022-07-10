from django.urls import path
from .views import my_home
from . import views as logic


urlpatterns = [
    path('', my_home, ""),
    path('my_home/', my_home, name="my_home"),

    path(route='get_vacancies/', view=logic.get_vacancies, name="get_vacancies"),
]

