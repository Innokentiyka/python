import json,abc
from vacancy import Vacancy

class FileHandler(abc.ABC):

    @abc.abstractmethod
    def save_vacancies(self, vacancies: list):
        pass

    @abc.abstractmethod
    def load_vacancies(self) -> list:
        pass

class JsonFileHandler(FileHandler):

    def init(self, filename: str):
        self.filename = filename

    def save_vacancies(self, vacancies: list):
        with open(self.filename, 'w') as f:
            json.dump([vars(vacancy) for vacancy in vacancies], f)

    def load_vacancies(self) -> list:
        with open(self.filename, 'r') as f:
            return [Vacancy(**data) for data in json.load(f)]