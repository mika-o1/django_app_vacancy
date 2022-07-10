import json

import requests
from django.shortcuts import render


def my_home(request):
    return render(request, 'app_heroku/pages/my_home.html')


def get_vacancies(request):
    context = {
    }
    if request.method == "POST":
        vacancie = request.POST.get("vacancie", "Никто")

        ##################################################

        # 1)  вытащить вакансии с api hh по выбранной вакансии с фронтенда

        params = {
            'text': f'NAME:{vacancie}',  # Текст фильтра. В имени должно быть слово "Аналитик"
            'area': 40,  # Поиск ощуществляется по вакансиям города Москва
            'page': 1,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        response = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        json_data1 = json.loads(response.content.decode())  # получаем весь объект запроса

        # 2) по необходимости - обработать эти данные

        vacancies = json_data1["items"]

        for i in vacancies:
            print(i)
            print("\n\n")

        print(f'длина: {len(vacancies)}')

        # 3) отправить полученные обработанные данные назад во фронтенд

        ##################################################

        print(vacancie)
        context = {
            "vacancie": vacancie,
            "vacancies": vacancies
        }
    return render(request, 'app_heroku/pages/VacanciesPage.html', context)