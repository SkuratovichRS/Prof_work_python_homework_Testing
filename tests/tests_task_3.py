import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager


class TestYandexAuth:
    def setup_method(self):
        self.chrome_path = ChromeDriverManager().install()
        self.options = ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument("--incognito")
        self.browser_service = Service(executable_path=self.chrome_path)
        self.browser = Chrome(service=self.browser_service, options=self.options)

    @pytest.mark.parametrize(
        "email, password, expected",
        (
                ["email", "password", "Неверный пароль"],
        )
    )
    def test_login_1(self, email, password, expected):
        self.browser.get("https://passport.yandex.ru/auth/")
        email_field = self.browser.find_element(by=By.CLASS_NAME, value="Textinput-Control")
        email_field.send_keys(email)
        button = self.browser.find_element(by=By.ID, value="passp:sign-in")
        button.click()
        password_field = WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located((By.NAME, "passwd")))
        password_field.send_keys(password)
        password_field.submit()
        error = WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "field:input-passwd:hint")))
        assert error.text == expected

    @pytest.mark.parametrize(
        "email, expected",
        (
                ["123", "Такой логин не подойдет"],
                ["ййй", "Такой логин не подойдет"],
        )
    )
    def test_login_2(self, email, expected):
        self.browser.get("https://passport.yandex.ru/auth/")
        email_field = self.browser.find_element(by=By.CLASS_NAME, value="Textinput-Control")
        email_field.send_keys(email)
        button = self.browser.find_element(by=By.ID, value="passp:sign-in")
        button.click()
        error = WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "field:input-login:hint")))
        assert error.text == expected

    @pytest.mark.parametrize(
        "email, password, expected",
        (
                ["your_correct_email", "your_correct_password", "https://id.yandex.ru/"],
        )
    )
    def test_login_3(self, email, password, expected):
        self.browser.get("https://passport.yandex.ru/auth/")
        email_field = self.browser.find_element(by=By.CLASS_NAME, value="Textinput-Control")
        email_field.send_keys(email)
        button = self.browser.find_element(by=By.ID, value="passp:sign-in")
        button.click()
        password_field = WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located((By.NAME, "passwd")))
        password_field.send_keys(password)
        password_field.submit()
        try:
            WebDriverWait(self.browser, 10).until(
                expected_conditions.url_matches(expected))
        except Exception as e:
            print(f"{e}")
        assert self.browser.current_url == expected
