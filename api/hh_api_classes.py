import requests
from api.abs_class import ABSTRACT

class HH_API(ABSTRACT):
    def __init__(self, vacancies):
        self.vacancies = vacancies
        self.__headers = {
            "User-Agent": "anonim_user"
        }
        self.__params = {
            'text': self.vacancies,
            'only_with_salary': True,
            'area_code': 'RU',
            'per_page': 100,
        }
        self.responce = requests.get("https://api.hh.ru/vacancies", params=self.__params, headers=self.__headers)
        self.responce_json = self.responce.json()['items']

    def get_responce(self):
        return self.responce_json


class HH_EMPLOYER(ABSTRACT):
    def __init__(self, employer_id):

        self.employer_id = employer_id
        self.__headers = {
            "User-Agent": "anonim_user"
        }
        self.__params = {
            'only_with_salary': True,
            'employer_id': self.employer_id,
            'per_page': 100
        }
        self.responce = requests.get("https://api.hh.ru/vacancies", params=self.__params, headers=self.__headers)
        self.responce_json = self.responce.json()['items']

    def get_responce(self):
        return self.responce_json
