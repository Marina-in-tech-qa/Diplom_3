
import allure

from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators


class ConstructorPage(BasePage):

    # Перейти в конструктор бургеров
    @allure.step("Перейти в конструктор")
    def click_constructor(self):
        self.click_element(
            ConstructorLocators.CONSTRUCTOR_BUTTON
        )

    # Перейти в ленту заказов
    @allure.step("Перейти в ленту заказов")
    def click_order_feed(self):
        self.click_element(
            ConstructorLocators.ORDER_FEED_BUTTON
        )

    # Открыть модальное окно ингредиента
    @allure.step("Открыть детали ингредиента")
    def open_ingredient_details(self):
        self.click_element(
            ConstructorLocators.INGREDIENT_CARD
        )

    # Получить заголовок модального окна ингредиента
    @allure.step("Получить заголовок деталей ингредиента")
    def get_ingredient_modal_title(self):
        return self.get_text(
            ConstructorLocators.INGREDIENT_MODAL_TITLE
        )

    # Закрыть модальное окно ингредиента
    @allure.step("Закрыть детали ингредиента")
    def close_ingredient_details(self):
        self.click_element(
            ConstructorLocators.INGREDIENT_MODAL_CLOSE
        )

    # Перетащить булку в корзину с помощью HTML5 Drag & Drop
    @allure.step("Перетащить булку в корзину")
    def drag_ingredient_to_basket(self):
        ingredient = self.find_element(
            ConstructorLocators.INGREDIENT_CARD
        )

        basket = self.find_element(
            ConstructorLocators.BURGER_BASKET
        )

        # Создать общий объект DataTransfer для событий переноса
        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();

            // Создать и отправить событие HTML5 Drag & Drop
            function dispatchDragEvent(element, type) {
                const event = new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });

                element.dispatchEvent(event);
            }

            // Начать перетаскивание ингредиента
            dispatchDragEvent(source, "dragstart");

            // Переместить ингредиент над корзиной
            dispatchDragEvent(target, "dragenter");
            dispatchDragEvent(target, "dragover");

            // Завершить перетаскивание
            dispatchDragEvent(target, "drop");
            dispatchDragEvent(source, "dragend");
        """, ingredient, basket)

    # Получить количество добавленных булок
    @allure.step("Получить счётчик ингредиента")
    def get_ingredient_counter(self):
        return int(
            self.get_text(
                ConstructorLocators.INGREDIENT_COUNTER
            )
        )

    # Нажать кнопку «Оформить заказ»
    @allure.step("Нажать кнопку оформления заказа")
    def click_order_button(self):
        self.click_element(
            ConstructorLocators.ORDER_BUTTON
        )

    # Получить настоящий номер оформленного заказа
    @allure.step("Получить номер оформленного заказа")
    def get_order_number(self):
        try:
            # Дождаться замены временного номера на настоящий
            order_number = self.wait.until(
                lambda browser: (
                    number
                    if (
                        number := self.get_text(
                            ConstructorLocators.ORDER_NUMBER
                        )
                    ).isdigit() and number != "9999"
                    else False
                ),
                message="Настоящий номер заказа не появился"
            )

            return int(order_number)

        except TimeoutException:
            # Вывести номер, оставшийся после ожидания
            current_number = self.get_text(
                ConstructorLocators.ORDER_NUMBER
            )

            print(
                f"Номер в модальном окне после ожидания: "
                f"{current_number}"
            )

            raise

    # Собрать бургер, оформить заказ и получить его номер
    @allure.step("Собрать бургер и оформить заказ")
    def create_order(self):
        self.drag_ingredient_to_basket()
        self.click_order_button()
        return self.get_order_number()
