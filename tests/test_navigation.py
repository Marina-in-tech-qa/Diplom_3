
import allure

from pages.constructor_page import ConstructorPage
from urls import BASE_URL


@allure.feature("Навигация")
class TestNavigation:

    # Проверить переход из конструктора в ленту заказов
    @allure.title("Переход из конструктора в ленту заказов")
    def test_go_to_order_feed(self, driver):
        page = ConstructorPage(driver)

        # Открыть главную страницу
        with allure.step("Открыть конструктор"):
            page.open(BASE_URL)

        # Перейти в ленту заказов
        with allure.step("Нажать кнопку «Лента заказов»"):
            page.click_order_feed()

        # Проверить переход в ленту заказов
        with allure.step("Проверить открытие ленты заказов"):
            assert page.is_order_feed_opened()

    # Проверить переход из ленты заказов в конструктор
    @allure.title("Переход из ленты заказов в конструктор")
    def test_go_to_constructor(self, driver):
        page = ConstructorPage(driver)

        # Открыть ленту заказов
        with allure.step("Открыть ленту заказов"):
            page.open(f"{BASE_URL}/feed")

        # Перейти в конструктор
        with allure.step("Нажать кнопку «Конструктор»"):
            page.click_constructor()

        # Проверить переход в конструктор
        with allure.step("Проверить открытие конструктора"):
            assert page.is_constructor_opened()
