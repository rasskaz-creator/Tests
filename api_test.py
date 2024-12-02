import requests
import pytest

TOKEN = ""
BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"

def create_folder(folder_name):
    headers = {"Authorization": f"OAuth {TOKEN}"}
    params = {"path": folder_name}
    response = requests.put(BASE_URL, headers=headers, params=params)
    return response

def check_folder_exists(folder_name):
    headers = {"Authorization": f"OAuth {TOKEN}"}
    params = {"path": folder_name}
    response = requests.get(BASE_URL, headers=headers, params=params)
    return response



@pytest.mark.parametrize("folder_name", ["test_folder"])
def test_create_folder_success(folder_name):
    response = create_folder(folder_name)
    assert response.status_code == 201 or response.status_code == 409, \
        f"Неверный код ответа: {response.status_code}, текст: {response.text}"

    response_check = check_folder_exists(folder_name)
    assert response_check.status_code == 200, \
        f"Папка не найдена: {response_check.status_code}, текст: {response_check.text}"


@pytest.mark.parametrize("folder_name, expected_status_code", [
    ("", 400),
    ("existing_folder", 409),
    ("/invalid/folder?name", 409),
])
def test_create_folder_error(folder_name, expected_status_code):
    response = create_folder(folder_name)
    assert response.status_code == expected_status_code, \
        f"Ожидали {expected_status_code}, получили {response.status_code}, текст: {response.text}"


def test_create_folder_invalid_token():
    invalid_token = "invalid_token"
    headers = {"Authorization": f"OAuth {invalid_token}"}
    params = {"path": "test_folder"}
    response = requests.put(BASE_URL, headers=headers, params=params)
    assert response.status_code == 401, \
        f"Ожидали 401, получили {response.status_code}, текст: {response.text}"