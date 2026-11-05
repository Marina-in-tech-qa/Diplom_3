
import allure

from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from urls import BASE_URL


@allure.feature("Лента заказов")
class TestOrderFeed:

    # Проверить увеличение общего счётчика после оформления заказа
    @allure.title("Увеличение общего счётчика после оформления заказа")
    def test_total_orders_increases(self, driver, created_user):
        feed_page = OrderFeedPage(driver)
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)

        # Получить количество заказов до оформления
        with allure.step("Получить общий счётчик заказов"):
            feed_page.open(f"{BASE_URL}/feed")
            total_before = feed_page.get_total_orders()

        # Авторизоваться под тестовым пользователем
        with allure.step("Авторизоваться"):
            login_page.open(f"{BASE_URL}/login")
            login_page.login(
                created_user["email"],
                created_user["password"]
            )

        # Собрать бургер и оформить заказ
        with allure.step("Оформить заказ"):
            constructor_page.create_order()

        # Проверить увеличение общего счётчика
        with allure.step("Проверить увеличение счётчика за всё время"):
            feed_page.open(f"{BASE_URL}/feed")
            assert feed_page.wait_for_total_orders_increase(total_before)

    # Проверить увеличение счётчика заказов за сегодня
    @allure.title("Увеличение счётчика заказов за сегодня")
    def test_today_orders_increases(self, driver, created_user):
        feed_page = OrderFeedPage(driver)
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)

        # Получить количество заказов за сегодня до оформления
        with allure.step("Получить счётчик заказов за сегодня"):
            feed_page.open(f"{BASE_URL}/feed")
            today_before = feed_page.get_today_orders()

        # Авторизоваться под тестовым пользователем
        with allure.step("Авторизоваться"):
            login_page.open(f"{BASE_URL}/login")
            login_page.login(
                created_user["email"],
                created_user["password"]
            )

        # Собрать бургер и оформить заказ
        with allure.step("Оформить заказ"):
            constructor_page.create_order()

        # Проверить увеличение счётчика за сегодня
        with allure.step("Проверить увеличение счётчика за сегодня"):
            feed_page.open(f"{BASE_URL}/feed")
            assert feed_page.wait_for_today_orders_increase(today_before)

    # Проверить появление оформленного заказа в разделе «В работе»
    @allure.title("Номер оформленного заказа появляется в разделе «В работе»")
    def test_order_appears_in_progress(self, driver, created_user):
        feed_page = OrderFeedPage(driver)
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)

        # Авторизоваться под тестовым пользователем
        with allure.step("Авторизоваться"):
            login_page.open(f"{BASE_URL}/login")
            login_page.login(
                created_user["email"],
                created_user["password"]
            )

        # Собрать бургер и получить номер заказа
        with allure.step("Оформить заказ и получить его номер"):
            order_number = constructor_page.create_order()

        # Открыть ленту заказов
        with allure.step("Перейти в ленту заказов"):
            feed_page.open(f"{BASE_URL}/feed")

        # Проверить появление заказа в разделе «В работе»
        with allure.step("Проверить номер заказа в разделе «В работе»"):
            assert feed_page.wait_for_order_in_progress(order_number)
