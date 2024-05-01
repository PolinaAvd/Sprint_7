import requests
import random
import string
import allure
import data

class Main:
    @allure.step('Генератор случайных числел')
    def generator_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step('Возвращаем регистационные данные')
    def register_new_courier_and_return_login_password(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login_pass = []

        login = self.generator_random_string(10)
        password = self.generator_random_string(10)
        first_name = self.generator_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(data.CREATE_COURER_URL, data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

            return login_pass


