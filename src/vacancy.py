
from dataclasses import dataclass
from typing import re


@dataclass
class Vacancy:
    name: str
    url: str
    salary: str
    requirements: str
    salary_from: int = None
    salary_to: int = None

    def __str__(self):
        """Вернуть название вакансии.

        return:
            название вакансии
        """
        return self.name

    def __repr__(self):
        """Вернуть название вакансии.

        return:
            название вакансии
        """
        return self.name

    def __gt__(self, other):
        """Сравнить вакансии по зарплате.

        Args:
            other (Vacancy): объект, с которым сравниваем текущий объект

        return:
            критерий сравнения
        """
        return self.avg_salary() > other.avg_salary()

    def parse_salary(self):
        salary_from, salary_to = re.findall(r'[\d\s]+', self.salary)
        self.salary_from = int(salary_from.replace(' ', ''))
        self.salary_to = int(salary_to.replace(' ', ''))

    def get_salary(self):
        if self.salary:
            self.parse_salary()
        else:
            if self.salary_from and self.salary_to:
                self.salary = '{0}-{1} руб.'.format(
                    self.salary_from, self.salary_to,
                )
            elif self.salary_from and not self.salary_to:
                self.salary = 'от {0} руб.'.format(self.salary_from)
            elif not self.salary_from and self.salary_to:
                self.salary = 'до {0} руб.'.format(self.salary_to)

    def avg_salary(self):
        """Вернуть зарплату по вакансии для сравнения.

        return:
            зарплату по вакансии для сравнения
        """
        if self.salary_from:
            return self.salary_from
        elif self.salary_to:
            return self.salary_to
        return 0

    def serialize(self):
        """Вернуть свойства объекта в виде словаря.

        return:
            свойства объекта в виде словаря
        """
        return self.__dict__
