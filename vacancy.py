class InvalidDataError(Exception):
    """Основное исключение для ошибок валидации"""

    def init(self, message, field=None):
        """
        :param message: Сообщение об ошибке.
        :param field: Поле, которое вызвало ошибку.
        """
        super().init(message)
        self.field = field

    def str(self):
        base_message = super().str()
        if self.field:
            return f"Field '{self.field}': {base_message}"
        return base_message

class Vacancy:
    def init(self, title: str, link: str, salary: str, description: str):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        if not value:
            raise InvalidDataError("Title cannot be empty.")
        self._title = value

    @property
    def link(self) -> str:
        return self._link

    @link.setter
    def link(self, value: str):
        if not value.startswith("http"):
            raise InvalidDataError("Invalid URL provided.")
        self._link = value

    @property
    def salary(self) -> str:
        return self._salary

    @salary.setter
    def salary(self, value: str):
        if not value:
            value = "Not specified"
        self._salary = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        if not value:
            raise InvalidDataError("Description cannot be empty.")
        self._description = value

    def lt(self, other):
        # Пример сравнения вакансий по зарплате. Детальная реализация зависит от формата данных о зарплате.
        return self.salary < other.salary