
import allure

from selenium.webdriver.support import expected_conditions as EC

from pages.constructor_page import ConstructorPage
from locators.constructor_locators import ConstructorLocators
from urls import BASE_URL


@allure.feature("Ингредиенты")
@allure.title("Открытие модального окна ингредиента")
def test_open_ingredient_modal(driver):
    page = ConstructorPage(driver)

    # Открыть конструктор
    with allure.step("Открыть конструктор"):
        page.open(BASE_URL)

    # Открыть карточку ингредиента
    with allure.step("Нажать на карточку ингредиента"):
        page.open_ingredient_details()

    # Проверить заголовок модального окна
    with allure.step("Проверить заголовок модального окна"):
        assert page.get_ingredient_modal_title() == "Детали ингредиента"


@allure.feature("Ингредиенты")
@allure.title("Закрытие модального окна ингредиента")
def test_close_ingredient_modal(driver):
    page = ConstructorPage(driver)

    # Открыть конструктор
    with allure.step("Открыть конструктор"):
        page.open(BASE_URL)

    # Открыть детали ингредиента
    with allure.step("Открыть детали ингредиента"):
        page.open_ingredient_details()

    # Закрыть модальное окно
    with allure.step("Закрыть модальное окно"):
        page.close_ingredient_details()

    # Проверить закрытие модального окна
    with allure.step("Проверить закрытие модального окна"):
        assert page.wait.until(
            EC.invisibility_of_element_located(
                ConstructorLocators.INGREDIENT_MODAL_TITLE
            )
        )


@allure.feature("Ингредиенты")
@allure.title("Увеличение счётчика при добавлении ингредиента")
def test_ingredient_counter_increases(driver):
    page = ConstructorPage(driver)

    # Открыть конструктор
    with allure.step("Открыть конструктор"):
        page.open(BASE_URL)

    # Перетащить булку в корзину
    with allure.step("Перетащить булку в корзину"):
        page.drag_ingredient_to_basket()

    # Проверить увеличение счётчика
    with allure.step("Проверить счётчик ингредиента"):
        page.wait.until(
            lambda browser: page.get_ingredient_counter() == 2
        )

        assert page.get_ingredient_counter() == 2
