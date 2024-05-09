def check_age(age: int):
    if age >= 18:
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'

    return result


def check_auth(login: str, password: str):
    if login == "admin" and password == "password":
        result = "Добро пожаловать"
    else:
        result = "Доступ ограничен"

    return result


def check_email(email: str) -> bool:
    if "@" in email and "." in email and " " not in email:
        return True
    return False
