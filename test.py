import pytest
from main import check_auth, check_email, solve


@pytest.mark.parametrize("login, password, expected_result", [
    ("admin", "password", "Добро пожаловать"),  # Правильные данные
    ("admin", "wrongpassword", "Доступ ограничен"),  # Неверный пароль
    ("user", "password", "Доступ ограничен"),  # Неверный логин
    ("", "", "Доступ ограничен"),  # Пустые логин и пароль
])
def test_check_auth(login, password, expected_result):
    assert check_auth(login, password) == expected_result


@pytest.mark.parametrize("email, expected_result", [
    ("user@example.com", True),  # Валидный email
    ("user.name@example.co.ru", True),  # Сложный валидный email
    ("userexample.com", False),  # Нет символа "@"
    ("user@example", False),  # Нет точки
    ("user@ example.com", False),  # Пробел внутри email
])
def test_check_email(email, expected_result):
    assert check_email(email) == expected_result
#
#
@pytest.mark.parametrize("hare_distances, turtle_distances, expected_result", [
    ([10, 20, 30], [15, 15, 20], "заяц"),
    ([10, 20, 30], [20, 30, 20], "черепаха"),
    ([10, 20, 30], [10, 20, 30], "одинаково"),
    ([], [10, 20], "черепаха"),
    ([10, 20], [], "заяц"),
    ([], [], "одинаково"),
])
def test_solve(hare_distances, turtle_distances, expected_result):
    assert solve(hare_distances, turtle_distances) == expected_result
