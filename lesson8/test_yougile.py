import pytest
import requests


base_url = 'https://ru.yougile.com/api-v2/'

token = None
new_company_id = None


# получаем токен и сохраняем в глобальную переменную
@pytest.fixture(scope="module")
def get_auth_token():
    global token
    keys = {
        "login": "31may97@mail.ru",
        "password": "T49/F)c;Za^?m(V",
        "companyId": "604e123c-f07b-4036-b2e1-f72797d59af8"
    }
    r = requests.post(base_url + 'auth/keys', json=keys)
    assert r.status_code == 201
    token = r.json()["key"]
    return token


# создаём новую компанию
@pytest.fixture(scope="module")
def create_new_company(get_auth_token):
    global new_company_id
    my_headers = {
        "Authorization": f"Bearer {get_auth_token}",
        "Content-Type": "application/json"
    }
    my_body = {
        "title": "TestCompany"
    }
    r = requests.post(base_url + 'projects', headers=my_headers, json=my_body)
    assert r.status_code == 201
    new_company_id = r.json().get("id")
    return new_company_id


# получение списка компаний
def test_get_companies_positive(get_auth_token):
    my_headers = {
        "Authorization": f"Bearer {get_auth_token}",
        "Content-Type": "application/json"
    }
    r = requests.get(base_url + 'projects', headers=my_headers)
    assert r.status_code == 200


# получение списка компаний без авторизации
def test_get_companies_no_auth_negative():
    r = requests.get(base_url + 'projects')
    assert r.status_code == 401


# создание новой компании без указания названия
def test_empty_title_company_negative(get_auth_token):
    my_headers = {
        "Authorization": f"Bearer {get_auth_token}",
        "Content-Type": "application/json"
    }
    body = {
        "title": None
    }
    r = requests.post(base_url + 'projects', headers=my_headers, json=body)
    assert r.status_code == 400


# изменение имени у созданной нами в начале компании
def test_update_name(get_auth_token, create_new_company):
    my_headers = {
        "Authorization": f"Bearer {get_auth_token}",
        "Content-Type": "application/json"
    }
    body = {
        "title": "NewTestCompany"
    }
    r = requests.put(base_url + "projects/" + create_new_company,
                     headers=my_headers, json=body)
    assert r.status_code == 200
    get_r = requests.get(base_url + "projects/" + create_new_company,
                         headers=my_headers)
    assert get_r.status_code == 200
    assert get_r.json().get("title") == "NewTestCompany"


# передаём неверный тип данных при изменении имени
def test_update_empty_name(get_auth_token, create_new_company):
    my_headers = {
        "Authorization": f"Bearer {get_auth_token}",
        "Content-Type": "application/json"
        }
    body = {
        "title": 111
    }
    r = requests.put(base_url + "projects/" + create_new_company,
                     headers=my_headers, json=body)
    assert r.status_code == 400


# получение компании по id
def test_get_company_by_id(get_auth_token, create_new_company):
    my_headers = {
        "Authorization": f"Bearer {get_auth_token}",
        "Content-Type": "application/json"
    }
    r = requests.get(base_url + "projects/" + create_new_company,
                     headers=my_headers)

    assert r.status_code == 200
    assert r.json().get("title") == "NewTestCompany"


# получение компании по пустому id
@pytest.mark.xfail(reason="API не корректно обрабатывает пустой ID в запросе")
def test_get_company_by_empty_id(get_auth_token):
    my_headers = {
        "Authorization": f"Bearer {get_auth_token}",
        "Content-Type": "application/json"
    }
    body = {
        "id": ""
    }
    r = requests.get(base_url + "projects/",
                     headers=my_headers, json=body)

    assert r.status_code == 404

# pytest test_yougile.py
