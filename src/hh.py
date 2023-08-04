import json
from pprint import pprint

import requests

from src.site_api import API


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

            self.to_json(vacancies, "json_hh.json")

            return vacancies

        else:
            print(f'Ошибка {response.status_code}')



    def get_10(self):
        return self.va[:10]

    def get_sorted(self):
        return sorted(self.va, key=lambda x: x['cost'])
