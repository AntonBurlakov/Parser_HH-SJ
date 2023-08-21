import requests

from src.json_saver import JSONSaver
from src.site_api import API
from src.vacancy import Vacancy


class HeadHunterAPI(API):
    def get_vacancies(self, keyword: str):

        """
        Получение вакансий
        :param keyword:
        :return:
        """

        url = "https://api.hh.ru/vacancies"

        params = {
            "text": keyword,
        }

        headers = {
            "User-Agent": "Your User Agent",
        }

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            vacancies = data.get("items")

            result = []
            json_saver = JSONSaver()

            for vacancy in vacancies:
                salary = vacancy.get('salary')
                salary_form = None
                salary_to = None
                if salary:
                    salary_form = salary['from']
                    salary_to = salary['to']
                vacancy_object = Vacancy(
                    vacancy['name'],
                    vacancy['alternate_url'],
                    "",
                    vacancy['snippet']['requirement'],
                    salary_form,
                    salary_to,
                )
                json_saver.add_vacancy(vacancy_object)
                result.append(vacancy_object)

            return result
        else:
            print(f'Ошибка {response.status_code}')
