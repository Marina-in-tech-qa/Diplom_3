
import allure

from selenium.webdriver.support.ui import WebDriverWait

from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from urls import BASE_URL


@allure.feature("Лента заказов")
@allure.title("Увеличение общего счётчика после оформления заказа")
def test_total_orders_increases(driver, created_user):
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
        order_number = constructor_page.create_order()
        assert order_number > 0

    # Проверить увеличение общего счётчика
    with allure.step("Проверить увеличение счётчика за всё время"):
        feed_page.open(f"{BASE_URL}/feed")

        feed_page.wait.until(
            lambda browser: feed_page.get_total_orders() > total_before
        )

        total_after = feed_page.get_total_orders()

        assert total_after > total_before


@allure.feature("Лента заказов")
@allure.title("Увеличение счётчика заказов за сегодня")
def test_today_orders_increases(driver, created_user):
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
        order_number = constructor_page.create_order()
        assert order_number > 0

    # Проверить увеличение счётчика за сегодня
    with allure.step("Проверить увеличение счётчика за сегодня"):
        feed_page.open(f"{BASE_URL}/feed")

        feed_page.wait.until(
            lambda browser: feed_page.get_today_orders() > today_before
        )

        today_after = feed_page.get_today_orders()

        assert today_after > today_before


@allure.feature("Лента заказов")
@allure.title("Номер оформленного заказа появляется в разделе «В работе»")
def test_order_appears_in_progress(driver, created_user):
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

    # Собрать бургер и оформить заказ
    with allure.step("Оформить заказ и получить его номер"):
        order_number = constructor_page.create_order()
        assert order_number > 0

    # Открыть ленту заказов
    with allure.step("Перейти в ленту заказов"):
        feed_page.open(f"{BASE_URL}/feed")

    # Проверить появление номера заказа в разделе «В работе»
    with allure.step("Проверить номер заказа в разделе «В работе»"):
        print(f"Номер оформленного заказа: {order_number}")
        print(
            f"Заказы в работе: "
            f"{repr(feed_page.get_in_progress_orders())}"
        )

        # Дождаться появления номера заказа
        WebDriverWait(driver, 60).until(
            lambda browser: any(
                item.strip().lstrip("0") == str(order_number)
                for item in feed_page.get_in_progress_orders().splitlines()
            ),
            message=(
                f"Заказ {order_number} не появился "
                f"в разделе «В работе»"
            )
        )

        # Проверить наличие номера в списке
        orders_in_progress = feed_page.get_in_progress_orders()

        assert any(
            item.strip().lstrip("0") == str(order_number)
            for item in orders_in_progress.splitlines()
        )
