import requests
import data
import allure

class ListOfOrders:

    @allure.step('Запрос списка')
    def get_orders(self):
        response = requests.get(data.GET_ORDER_URL)
        r = response.json()
        return r


