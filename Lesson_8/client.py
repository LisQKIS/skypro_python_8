import requests
import json
from Lesson_8.constants import X_client_URL



path = '/employee/'

class Company:
    def __init__(self, url=X_client_URL):
        self.url = url


#создание компании
class Company:
    def __init__(self, url=X_client_URL):
        self.url = url

    def create(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(self.url + '/company', headers=headers, json=body)
        return response.json()
    
    def last_active_company_id(self):
        active_params = {"active":"true"}
        response = requests.get(self.url +'/company',params= active_params)
        return response.json()[-1]['id']
    


class Employer:
    def __init__(self, url=X_client_URL):
        self.url = url
    # список сотрудников компании
    def get_list(self, company_id: int):
        company = {'company':company_id}
        response = requests.get(self.url + '/employee', params=company)
        return response.json()

    # добавление сотрудника
    def add_new(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(self.url + '/employee', headers=headers, json=body)
        return response.json()

    # получение информации
    def get_info(self, employee_id: int):
        response = requests.get(self.url + path + str(employee_id))
        return response

    # изменение информации
    def chanqe_info(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token': token}
        response = requests.patch(self.url + path + str(employee_id), headers=headers, json=body)
        return response