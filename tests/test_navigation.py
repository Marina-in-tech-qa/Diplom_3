
import allure

from pages.constructor_page import ConstructorPage
from urls import BASE_URL


@allure.feature("Навигация")
@allure.title("Переход из конструктора в ленту заказов")
def test_go_to_order_feed(driver):
    page = ConstructorPage(driver)

    # Открыть главную страницу
    with allure.step("Открыть конструктор"):
        page.open(BASE_URL)

    # Перейти в ленту заказов
    with allure.step("Нажать кнопку «Лента заказов»"):
        page.click_order_feed()

    # Проверить переход
    with allure.step("Проверить открытие ленты заказов"):
        page.wait.until(
            lambda browser: browser.current_url.rstrip("/")
            == f"{BASE_URL}/feed"
        )

        assert driver.current_url.rstrip("/") == f"{BASE_URL}/feed"


@allure.feature("Навигация")
@allure.title("Переход из ленты заказов в конструктор")
def test_go_to_constructor(driver):
    page = ConstructorPage(driver)

    # Открыть ленту заказов
    with allure.step("Открыть ленту заказов"):
        page.open(f"{BASE_URL}/feed")

    # Перейти в конструктор
    with allure.step("Нажать кнопку «Конструктор»"):
        page.click_constructor()

    # Проверить переход
    with allure.step("Проверить открытие конструктора"):
        page.wait.until(
            lambda browser: browser.current_url.rstrip("/")
            == BASE_URL
        )

        assert driver.current_url.rstrip("/") == BASE_URL
