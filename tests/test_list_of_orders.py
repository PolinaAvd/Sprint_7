from pages.list_of_orders import *
import allure


class TestListOfOrders():

    @allure.title('В тело ответа возвращается список заказов')
    def test_list_of_orders_consist_lists(self):
        response = ListOfOrders().get_orders()
        assert type(response) == dict and "orders" in response



