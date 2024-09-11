import requests
import json
import pytest
from Lesson_8.constants import X_client_URL
from Lesson_8.Pages.Employee import Employer,Company


employer = Employer()
company = Company()



def test_authorization(get_token):
    token = get_token
    assert token is not None
    assert isinstance(token,str)

def test_getcompany_id():
    company_id = company.last_active_company_id
    assert company_id is not None
    assert str(company_id).isdigit
       
def test_add_employer(get_token):
    token=str(get_token)
    com_id= company.last_active_company_id()
    body_employer= {
        "id": 0,
  "firstName": "Keks",
  "lastName": "Petrof",
  "middleName": "string",
  "companyId":  com_id,
  "email": "tetst@yandex.ru",
  "url": "string",
  "phone": "string",
  "birthdate": "2024-09-05T10:28:13.060Z",
  "isActive": True
    }
    nwe_employer_id=(employer.add_new(token,body_employer))['id']
    assert nwe_employer_id is not None
    assert str(nwe_employer_id).isdigit()

def test_get_employer ():
    com_id=company.last_active_company_id()
    list_employers= employer.get_list(com_id)
    assert isinstance(list_employers,list)

def test_change_employer_info(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()

    body_employer = {
        "firstName": "Keks",
        "lastName": "Petrov",
        "middleName": "string",
        "companyId": com_id,
        "email": "tetst@yandex.ru",
        "url": "string",
        "phone": "string",
        "birthdate": "2024-09-05T10:28:13.060Z",
        "isActive": True
    }

    # Добавляем нового сотрудника
    just_employer = employer.add_new(token, body_employer)
    id = just_employer['id']

    body_change_employer = {
        "lastName": "Vasin",
        "email": "tetst3@yandex.ru",
        "url": "string",
        "phone": "string",
        "isActive": True
    }

    # Изменяем информацию о работодателе
    employer_change = employer.chanqe_info(token, id, body_change_employer)
    assert employer_change.status_code == 200
    assert id == employer_change.json()['id']
    assert(employer_change.json()["email"]) == body_change_employer.get("email")
                                        