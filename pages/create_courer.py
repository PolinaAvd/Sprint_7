from pages.main import Main
import requests
import data
import allure

class CreateCourer():

    @allure.step('Создание курьера')
    def courer_can_be_created(self):
        response = Main()
        reply = response.register_new_courier_and_return_login_password()
        return reply

    @allure.step('Создание двух одинаковых курьеров')
    def creation_of_doubled_courer(self):
        response = Main()
        saved_data = response.register_new_courier_and_return_login_password()
        payload = {
            "login": saved_data[0],
            "password": saved_data[1],
            "firstName": saved_data[2]
        }
        response_two = requests.post(data.CREATE_COURER_URL, data=payload)
        return response_two

    @allure.step('Чтобы создать курьера, нужно передать в ручку все обязательные поля')
    def creation_of_the_courer_no_data(self, payload):
        payload = payload
        response = requests.post(data.CREATE_COURER_URL, data=payload)
        return response

    @allure.step('Запрос возвращает правильный код ответа и текст')
    def creation_of_a_new_courer(self):
        response = Main()
        login = response.generator_random_string(10)
        password = response.generator_random_string(10)
        first_name = response.generator_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(data.CREATE_COURER_URL, data=payload)
        return response

    @allure.step('Если нет логина, запрос возвращает ошибку')
    def creation_of_the_courer_no_login(self):
        response = Main()
        password = response.generator_random_string(10)
        first_name = response.generator_random_string(10)
        payload = {
            "login": '',
            "password": password,
            "firstName": first_name
        }
        response = requests.post(data.CREATE_COURER_URL, data=payload)
        return response

    @allure.step('Если нет пароля, запрос возвращает ошибку')
    def creation_of_the_courer_no_password(self):
        response = Main()
        login = response.generator_random_string(10)
        first_name = response.generator_random_string(10)
        payload = {
            "login": login,
            "password": '',
            "firstName": first_name
        }
        response = requests.post(data.CREATE_COURER_URL, data=payload)
        return response

    @allure.step(
        'Если нет имени, запрос отрабатывает успешно - БАГ, по докумендации поле firstname е является опциоанальным')
    def creation_of_the_courer_no_firstname(self):
        response = Main()
        login = response.generator_random_string(10)
        password = response.generator_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": ''
        }
        response = requests.post(data.CREATE_COURER_URL, data=payload)
        return response

    @allure.step('Если создать пользователя с логином, который уже есть, возвращается ошибка')
    def creation_of_doubled_login_courer(self):
        response = Main()
        password = response.generator_random_string(10)
        firstName = response.generator_random_string(10)
        saved_data = response.register_new_courier_and_return_login_password()
        payload = {
            "login": saved_data[0],
            "password": password,
            "firstName": firstName
        }
        response_two = requests.post(data.CREATE_COURER_URL, data=payload)
        return response_two
