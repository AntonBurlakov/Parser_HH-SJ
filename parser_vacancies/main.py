from src.hh import HeadHunterAPI
from src.sj import SuperJobAPI
from src.vacancy import Vacancy
from src.json_saver import JSONSaver


def filter_vacancies(vacancies: list[Vacancy], filter_words: list[str]):
    vacancies_filtered = []
    for vac in vacancies:
        for query in filter_words:
            if query.lower() not in vac.name.lower():
                break
        else:
            vacancies_filtered.append(vac)

    return vacancies_filtered


def sort_vacancies(vacancies: list[Vacancy]):
    return sorted(vacancies)


def get_top_vacancies(vacancies: list[Vacancy], top_n):
    return sort_vacancies(vacancies)[::-1][:top_n]


def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy.name, vacancy.salary, vacancy.url)


def user_interaction():
    while True:
        platforms = input('С какой платформой будем работать?'
                           '\nHH - введите 1'
                           '\nSJ - введите 2'
                           '\nОбе - введите 3\n').strip()
        if platforms in '13':
            hh_api = HeadHunterAPI()
        if platforms in '23':
            sj_api = SuperJobAPI()
        if platforms not in '123':
            print('Введите число...')
        else:
            break
    query = input('Введите название вакансии: ').strip().lower()
    vacancies = []
    if platforms in '13':
        vacancies += hh_api.get_vacancies(query)
    if platforms in '23':
        vacancies += sj_api.get_vacancies(query)

    print("Найдно вакансий: {}".format(len(vacancies)))

    salary_query = input('Введите диапазон зарплат через тире: ')
    json_saver = JSONSaver()
    filtered_by_salary_vac = json_saver.get_vacancies_by_salary(salary_query)
    print("Найдно вакансий: {}".format(len(filtered_by_salary_vac)))
    filter_query = input('Введите дополнительные поисковые запросы (фильтры) '
                         'через запятую: '
                         ).strip().lower().split(', ')
    filtered_vac = filter_vacancies(filtered_by_salary_vac, filter_query)
    if filtered_vac:
        print("Найдно вакансий: {}".format(len(filtered_vac)))
        print("Нет вакансий, соответствующих заданным критериям.")
        if len(filtered_vac) > 0:
            try:
                vac_count = int(input('Сколько вакансий показать? '))
            except ValueError:
                vac_count = 5
            print_vacancies(get_top_vacancies(filtered_vac, vac_count))

    else:
        print("Нет вакансий, соответствующих заданным критериям.")


if __name__ == '__main__':
    user_interaction()
