from abc import ABC

from src.site_api import API


class Vacancy(API):
    def __init__(self, path):
        self.path = path
        self.vacancies = self.get_vacancies(keyword='')
        self.name = self.vacancies["profession"]
        self.url = self.vacancies["client"]["link"]
        self.salary_from = self.vacancies["payment_from"]
        self.salary_to = self.vacancies["payment_to"]
        self.salary = f'{self.salary_from} - {self.salary_to}'
        self.requirements = self.vacancies["experience"]

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary








#vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")