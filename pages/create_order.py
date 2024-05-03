import requests
import data
import json
import allure

class CreateOrder:

    @allure.step('Создание заказа')
    def creation_of_order(self, order_param):
        json_string = json.dumps(order_param)
        response = requests.post(data.CREATE_ORDER_URL, data=json_string)
        return response

