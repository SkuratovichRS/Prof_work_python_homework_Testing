import pytest
from task_1 import check_age, check_auth, check_email


@pytest.mark.parametrize(
    "age, expected",
    (
            [18, "Доступ разрешён"],
            [25, "Доступ разрешён"],
            [15, "Доступ запрещён"]
    )
)
def test_check_age(age, expected):
    actual = check_age(age)
    assert actual == expected


@pytest.mark.parametrize(
    "login, password, expected",
    (
            ["admin", "password", "Добро пожаловать"],
            ["adminn", "password", "Доступ ограничен"],
            ["admin", "passwordd", "Доступ ограничен"]
    )
)
def test_check_auth(login, password, expected):
    actual = check_auth(login, password)
    assert actual == expected


@pytest.mark.parametrize(
    "email, expected",
    (
            ["netology@yandex.ru", True],
            ["netology@yandex. ru", False],
            ["netology.yandex.ru", False],
            ["netology@yandex", False]
    )
)
def test_check_email(email, expected):
    actual = check_email(email)
    assert actual == expected
