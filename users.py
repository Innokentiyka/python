from APIH import HhAPI, SuperjobAPI
from vacancy import Vacancy
from File import JsonFileHandler


def user_interaction():
    print("Выберите платформу для поиска вакансий (1 - hh.ru, 2 - superjob.ru): ")
    platform_choice = input()
    print("Введите поисковый запрос: ")
    query = input()

    api = None
    if platform_choice == '1':
        api = HhAPI()
    elif platform_choice == '2':
        api = SuperjobAPI()

    vacancies_data = api.fetch_vacancies(query)

    vacancies = [Vacancy(v['name'], v['url'], v.get('salary', 'N/A'), v.get('description', 'N/A')) for v in
                 vacancies_data ]


    # Сохраняем в файл
    handler = JsonFileHandler('vacancies.json')
    handler.save_vacancies(vacancies)

    # Выводим результаты
    for v in vacancies:
        print(v.title, v.salary)
