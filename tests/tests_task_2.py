import configparser
import requests

config = configparser.ConfigParser()
config.read("token.ini")


class TestYandexDisk:

    def setup_method(self):
        self.url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.headers = {"authorization": config["TOKEN"]["ya_token"]}
        self.params = {"path": "test_dir"}

    def teardown_method(self):
        requests.delete(url=self.url, headers=self.headers, params=self.params)

    def test_create_dir_1(self):
        response = requests.put(url=self.url, headers=self.headers, params=self.params)
        assert response.status_code == 201

    def test_create_dir_2(self):
        params = {"pathh": "test_dir"}
        response = requests.put(url=self.url, headers=self.headers, params=params)
        assert response.status_code == 400

    def test_create_dir_3(self):
        headers = {"authorization": "token"}
        response = requests.put(url=self.url, headers=headers, params=self.params)
        assert response.status_code == 401
