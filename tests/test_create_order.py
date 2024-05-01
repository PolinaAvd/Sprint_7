from pages.create_order import CreateOrder
import data
import pytest
import allure
class TestCreateOrder():

    @allure.title('Создание заказа: с параметром блэк, с параметром грей, с обоими параметрами, без цвета')
    @pytest.mark.parametrize('order_param', [data.order_param_black, data.order_param_grey, data.order_param_black_and_grey, data.order_param_no_color])
    def test_order_is_created_with_black_color(self, order_param):
        response = CreateOrder().creation_of_order(order_param)
        assert response.status_code == 201

    @allure.title('Тело ответа содержит track')
    def test_order_with_track_in_response(self):
        response = CreateOrder().creation_of_order(data.order_param_black)
        assert 'track' in response.text

