from src.json_saver import JSONSaver
from src.site_api import API
import os
import requests
from dotenv import load_dotenv

from src.vacancy import Vacancy

load_dotenv()


class SuperJobAPI(API):

    def get_vacancies(self, keyword: str):
        """
        Получение вакансий
        :param keyword:
        :return:
        """
        url = 'api.superjob.ru'
        API_KEY_SJ = os.getenv("API_KEY_SJ")

        headers = {
            'Host': url,
            'X-Api-App-Id': API_KEY_SJ,
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        params = {'keyword': keyword}

        response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            vacancies = data.get("objects")

            result = []
            json_saver = JSONSaver()
            for vacancy in vacancies:
                vacancy_object = Vacancy(
                    vacancy['profession'],
                    vacancy['link'],
                    "",
                    vacancy['experience']['title'],
                    vacancy['payment_from'],
                    vacancy['payment_to'],
                )
                json_saver.add_vacancy(vacancy_object)
                result.append(vacancy_object)

            return result
        else:
            print(f'Ошибка {response.status_code}')
