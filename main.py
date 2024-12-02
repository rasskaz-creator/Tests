def check_auth(login: str, password: str):
    if login == 'admin' and password == 'password':
        result = 'Добро пожаловать'
    else:
        result = 'Доступ ограничен'

    return result

def check_email(email: str) -> bool:
    if ' ' in email:
        return False
    if '@' not in email:
        return False
    if '.' not in email:
        return False
    return True

def solve(hare_distances: list, turtle_distances: list):
    hare_all = 0
    for distance in hare_distances:
        hare_all += distance
    turtle_all = 0
    for distance in turtle_distances:
        turtle_all += distance
    if hare_all > turtle_all:
        result = "заяц"
    elif hare_all < turtle_all:
        result = "черепаха"
    else:
        result = "одинаково"
    return result


