from pprint import pprint

import requests


def get_vacancies(key_word):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": key_word,
    }
    headers = {
        "User-Agent": "Your User Agent",
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items")

        pprint(vacancies)


if __name__ == '__main__':
    print(get_vacancies("python"))
