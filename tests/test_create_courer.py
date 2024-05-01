import pytest
import data
from pages.create_courer import CreateCourer
import allure

class TestCreateCourer():

    @allure.title('Курьер может быть создан')
    def test_creation_of_a_new_courer(self):
        response = CreateCourer().courer_can_be_created()
        assert len(response) == 3

    @allure.title('Нельзя создать двух одинpаковых курьеров')
    def test_creation_of_doubled_courer_impossible(self):
        response = CreateCourer().creation_of_doubled_courer()
        assert response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

    @allure.title('Чтобы создать курьера, нужно передать в ручку все обязательные поля')
    @pytest.mark.parametrize('payload', [data.registration_no_data])
    def test_creation_of_the_courer_no_data_fail(self, payload):
        response = CreateCourer().creation_of_the_courer_no_data(payload)
        assert response.text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

    @allure.title('Запрос возвращает правильный код ответа')
    def test_creation_of_a_new_courer_corect_code(self):
        response = CreateCourer().creation_of_a_new_courer()
        assert response.status_code == 201

    @allure.title('Запрос возвращает правильный текст ответа')
    def test_creation_of_a_new_courer_corect_response(self):
        response = CreateCourer().creation_of_a_new_courer()
        assert response.text == '{"ok":true}'

    @allure.title('Если нет логина, запрос возвращает ошибку')
    def test_creation_of_the_courer_no_login_fail(self):
        response = CreateCourer().creation_of_the_courer_no_login()
        assert response.text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

    @allure.title('Если нет пароля, запрос возвращает ошибку')
    def test_creation_of_the_courer_no_password_fail(self):
        response = CreateCourer().creation_of_the_courer_no_password()
        assert response.text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

    @allure.title('Если нет имени, запрос отрабатывает успешно - БАГ, по докумендации поле firstname е является опциоанальным')
    def test_creation_of_the_courer_no_firstname_success(self):
        response = CreateCourer().creation_of_the_courer_no_firstname()
        assert response.text == '{"ok":true}' and response.status_code == 201

    @allure.title('Если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_creation_of_doubled_login_courer_fail(self):
        response = CreateCourer().creation_of_doubled_login_courer()
        assert response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
