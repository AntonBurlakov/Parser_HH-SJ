import json
from abc import abstractmethod, ABC
from pprint import pprint

import requests


class API(ABC):
    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass

    @staticmethod
    def to_json(data, path):
        with open(path, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
