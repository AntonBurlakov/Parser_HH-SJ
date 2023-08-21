from abc import abstractmethod, ABC

from src.vacancy import Vacancy


class API(ABC):
    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass


class FileAPI(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary: str):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def writer(self, data):
        pass

    @abstractmethod
    def reader(self):
        pass
