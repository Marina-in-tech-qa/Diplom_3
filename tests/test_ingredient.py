
import allure

from pages.constructor_page import ConstructorPage
from urls import BASE_URL


@allure.feature("Ингредиенты")
class TestIngredient:

    # Проверить открытие модального окна ингредиента
    @allure.title("Открытие модального окна ингредиента")
    def test_open_ingredient_modal(self, driver):
        page = ConstructorPage(driver)

        with allure.step("Открыть конструктор"):
            page.open(BASE_URL)

        with allure.step("Открыть карточку ингредиента"):
            page.open_ingredient_details()

        with allure.step("Проверить заголовок модального окна"):
            assert page.get_ingredient_modal_title() == (
                "Детали ингредиента"
            )

    # Проверить закрытие модального окна ингредиента
    @allure.title("Закрытие модального окна ингредиента")
    def test_close_ingredient_modal(self, driver):
        page = ConstructorPage(driver)

        with allure.step("Открыть конструктор"):
            page.open(BASE_URL)

        with allure.step("Открыть детали ингредиента"):
            page.open_ingredient_details()

        with allure.step("Закрыть модальное окно"):
            page.close_ingredient_details()

        with allure.step("Проверить закрытие модального окна"):
            assert page.is_ingredient_modal_closed()

    # Проверить увеличение счётчика при добавлении ингредиента
    @allure.title("Увеличение счётчика при добавлении ингредиента")
    def test_ingredient_counter_increases(self, driver):
        page = ConstructorPage(driver)

        with allure.step("Открыть конструктор"):
            page.open(BASE_URL)

        with allure.step("Перетащить булку в корзину"):
            page.drag_ingredient_to_basket()

        with allure.step("Проверить счётчик ингредиента"):
            assert page.wait_for_ingredient_counter(2) == 2
