
import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    # Получить количество выполненных заказов за всё время
    @allure.step("Получить количество заказов за всё время")
    def get_total_orders(self):
        return int(
            self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER)
        )

    # Получить количество выполненных заказов за сегодня
    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders(self):
        return int(
            self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER)
        )

    # Получить список номеров заказов в работе
    @allure.step("Получить список заказов в работе")
    def get_in_progress_orders(self):
        orders_list = self.find_element(
            OrderFeedLocators.IN_PROGRESS_ORDERS
        )
        return orders_list.text

    # Дождаться увеличения общего счётчика заказов
    @allure.step("Дождаться увеличения общего счётчика заказов")
    def wait_for_total_orders_increase(self, previous_count):
        try:
            return bool(
                self.wait.until(
                    lambda browser: (
                        self.get_total_orders() > previous_count
                    ),
                    message="Общий счётчик заказов не увеличился"
                )
            )
        except TimeoutException:
            return False

    # Дождаться увеличения счётчика заказов за сегодня
    @allure.step("Дождаться увеличения счётчика заказов за сегодня")
    def wait_for_today_orders_increase(self, previous_count):
        try:
            return bool(
                self.wait.until(
                    lambda browser: (
                        self.get_today_orders() > previous_count
                    ),
                    message="Счётчик заказов за сегодня не увеличился"
                )
            )
        except TimeoutException:
            return False

    # Проверить наличие номера заказа среди заказов в работе
    def is_order_in_progress(self, order_number):
        return any(
            item.strip().lstrip("0") == str(order_number)
            for item in self.get_in_progress_orders().splitlines()
        )

    # Дождаться появления номера заказа в разделе «В работе»
    @allure.step("Дождаться появления заказа №{order_number} в работе")
    def wait_for_order_in_progress(self, order_number):
        try:
            return bool(
                WebDriverWait(self.driver, 60).until(
                    lambda browser: self.is_order_in_progress(order_number),
                    message=(
                        f"Заказ {order_number} не появился "
                        f"в разделе «В работе»"
                    )
                )
            )
        except TimeoutException:
            return False
