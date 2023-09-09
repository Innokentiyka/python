import abc,requests



class VacancyAPI(abc.ABC):
    @abc.abstractmethod
    def fetch_vacancies(self, search_query: str) -> list:
        pass


class HhAPI(VacancyAPI):
    API_URL = 'https://api.hh.ru/vacancies'

    def fetch_vacancies(self, search_query: str) -> list:
        response = requests.get(self.API_URL, params={'text': search_query})
        return response.json().get('items', [])


class SuperjobAPI(VacancyAPI): #КЛЮЧ API НЕ НАШЁЛ
    API_URL = 'https://api.superjob.ru/2.0/vacancies/'
    HEADERS = {
        'Authorization': 'SECRET_KEY'
    }

    def fetch_vacancies(self, search_query: str) -> list:
        response = requests.get(self.API_URL, headers=self.HEADERS, params={'keywords': search_query})
        return response.json().get('objects', [])