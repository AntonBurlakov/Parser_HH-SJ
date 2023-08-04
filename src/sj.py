import json
import os
from pprint import pprint

import requests

from dotenv import load_dotenv

from src.site_api import API

load_dotenv()


class SuperJobAPI(API):

    def get_vacancies(self, keyword: str):
        """
        Получение вакансий
        :param keyword:
        :return:
        """
        url = 'api.superjob.ru'
        #        API_KEY_SJ = os.getenv("API_KEY_SJ")

        headers = {
            'Host': url,
            'X-Api-App-Id': 'v3.r.137707170.c3416a419fb31211a17d5e9c93d7c48a831bc0c4.99ca31577d6d5014f266b34d0ad0fb495a75c9c4',
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        params = {'keyword': keyword}

        response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            vacancies = data.get("objects")

            self.to_json(vacancies, "json_js.json")

            return vacancies

        else:
            print(f'Ошибка {response.status_code}')




