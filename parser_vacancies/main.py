from pprint import pprint

from src.hh import HeadHunterAPI
from src.sj import SuperJobAPI
from src.vacancy import Vacancy

# from src.sj import request_super_job


if __name__ == '__main__':
#    q = SuperJobAPI()
#    (q.get_vacancies('python'))

#    q = HeadHunterAPI()
#    (q.get_vacancies('python'))

    w = Vacancy()
    print(w.get_vacancies('python'))

