
import allure

from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators
from urls import BASE_URL


class ConstructorPage(BasePage):

    # Перейти в конструктор бургеров
    @allure.step("Перейти в конструктор")
    def click_constructor(self):
        self.click_element(ConstructorLocators.CONSTRUCTOR_BUTTON)

    # Перейти в ленту заказов
    @allure.step("Перейти в ленту заказов")
    def click_order_feed(self):
        self.click_element(ConstructorLocators.ORDER_FEED_BUTTON)

    # Проверить открытие ленты заказов
    @allure.step("Проверить открытие ленты заказов")
    def is_order_feed_opened(self):
        return self.is_url_opened(f"{BASE_URL.rstrip('/')}/feed")

    # Проверить открытие конструктора бургеров
    @allure.step("Проверить открытие конструктора")
    def is_constructor_opened(self):
        return self.is_url_opened(BASE_URL)

    # Открыть модальное окно ингредиента
    @allure.step("Открыть детали ингредиента")
    def open_ingredient_details(self):
        self.click_element(ConstructorLocators.INGREDIENT_CARD)

    # Получить заголовок модального окна ингредиента
    @allure.step("Получить заголовок деталей ингредиента")
    def get_ingredient_modal_title(self):
        return self.get_text(ConstructorLocators.INGREDIENT_MODAL_TITLE)

    # Закрыть модальное окно ингредиента
    @allure.step("Закрыть детали ингредиента")
    def close_ingredient_details(self):
        self.click_element(ConstructorLocators.INGREDIENT_MODAL_CLOSE)

    # Проверить, что модальное окно ингредиента закрылось
    @allure.step("Дождаться закрытия модального окна ингредиента")
    def is_ingredient_modal_closed(self):
        return self.wait.until(
            EC.invisibility_of_element_located(
                ConstructorLocators.INGREDIENT_MODAL_TITLE
            )
        )

    # Перетащить булку в корзину с помощью HTML5 Drag & Drop
    @allure.step("Перетащить булку в корзину")
    def drag_ingredient_to_basket(self):
        self.drag_and_drop(
            ConstructorLocators.INGREDIENT_CARD,
            ConstructorLocators.BURGER_BASKET
        )

    # Получить количество добавленных булок
    @allure.step("Получить счётчик ингредиента")
    def get_ingredient_counter(self):
        return int(
            self.get_text(ConstructorLocators.INGREDIENT_COUNTER)
        )

    # Дождаться нужного значения счётчика ингредиента
    @allure.step("Дождаться значения счётчика ингредиента: {expected_count}")
    def wait_for_ingredient_counter(self, expected_count):
        return self.wait.until(
            lambda browser: (
                count
                if (count := self.get_ingredient_counter()) == expected_count
                else False
            ),
            message=f"Счётчик ингредиента не достиг значения {expected_count}"
        )

    # Нажать кнопку «Оформить заказ»
    @allure.step("Нажать кнопку оформления заказа")
    def click_order_button(self):
        self.click_element(ConstructorLocators.ORDER_BUTTON)

    # Получить настоящий номер оформленного заказа
    @allure.step("Получить номер оформленного заказа")
    def get_order_number(self):
        order_number = self.wait.until(
            lambda browser: (
                number
                if (
                    number := self.get_text(ConstructorLocators.ORDER_NUMBER)
                ).isdigit() and number != "9999"
                else False
            ),
            message="Настоящий номер заказа не появился"
        )
        return int(order_number)

    # Собрать бургер, оформить заказ и получить его номер
    @allure.step("Собрать бургер и оформить заказ")
    def create_order(self):
        self.drag_ingredient_to_basket()
        self.click_order_button()
        return self.get_order_number()
