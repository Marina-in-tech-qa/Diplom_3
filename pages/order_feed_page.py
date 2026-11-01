
import allure

from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    # Получить количество выполненных заказов за всё время
    @allure.step("Получить количество заказов за всё время")
    def get_total_orders(self):
        return int(
            self.get_text(
                OrderFeedLocators.TOTAL_ORDERS_COUNTER
            )
        )

    # Получить количество выполненных заказов за сегодня
    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders(self):
        return int(
            self.get_text(
                OrderFeedLocators.TODAY_ORDERS_COUNTER
            )
        )

    # Получить список номеров заказов в работе
    @allure.step("Получить список заказов в работе")
    def get_in_progress_orders(self):
        orders_list = self.find_element(
            OrderFeedLocators.IN_PROGRESS_ORDERS
        )
        return orders_list.text
