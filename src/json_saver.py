import json
from pathlib import Path
import re

from src.site_api import FileAPI
from src.vacancy import Vacancy


class JSONSaver(FileAPI):
    def __init__(self):
        self.path = 'vacancies.json'
        if not Path(self.path).exists():
            with open(self.path, 'w', encoding='utf8') as f:
                f.write('[]')

    def add_vacancy(self, vacancy: Vacancy):
        vacancies = self.reader()
        if vacancy.url not in [vac['url'] for vac in vacancies]:
            vacancies.append(vacancy.serialize())
            self.writer(vacancies)

    def get_vacancies_by_salary(self, salary: str):
        salary_from, salary_to = re.findall(r'[\d\s]+', salary)
        salary_from = int(salary_from.replace(' ', ''))
        salary_to = int(salary_to.replace(' ', ''))
        vacancies = self.reader()
        result = []
        for vacancy in vacancies:
            if (vacancy['salary_from'] and vacancy['salary_to']
                    and vacancy['salary_from'] >= salary_from
                    and vacancy['salary_to'] <= salary_to):
                result.append(Vacancy(**vacancy))
        return result

    def delete_vacancy(self, vacancy: Vacancy):
        vacancies = self.reader()
        vacancies_count_before = len(vacancies)
        vacancies = [vac for vac in vacancies if vac['url'] != vacancy.url]
        vacancies_count_after = len(vacancies)
        if vacancies_count_before != vacancies_count_after:
            self.writer(vacancies)

    def writer(self, data: list[dict]):
        with open(self.path, 'w', encoding='utf8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def reader(self):
        with open(self.path, 'r', encoding='utf8') as f:
            return json.loads(f.read())
