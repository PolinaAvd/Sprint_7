import allure

from pages.main import Main
import requests
import data


class CourerLogIn(Main):

    @allure.step('Авторизация курьера после создания')
    def courer_authorization_after_creation(self):
        saved_data = self.register_new_courier_and_return_login_password()
        payload = {
            "login": saved_data[0],
            "password": saved_data[1]
        }
        response = requests.post(data.LOGIN_COURER_URL, data=payload)
        return response

