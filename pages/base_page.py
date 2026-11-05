
import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)


class BasePage:

    # Инициализировать драйвер и ожидание элементов
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Открыть страницу по указанному адресу
    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    # Найти видимый элемент на странице
    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    # Дождаться доступности элемента и нажать на него
    def click_element(self, locator):

        # Проверить доступность элемента и выполнить обычный клик
        def click_when_available(driver):
            try:
                element = driver.find_element(*locator)

                if not element.is_displayed() or not element.is_enabled():
                    return False

                # Проверить отсутствие перекрытия в центре элемента
                is_accessible = driver.execute_script("""
                    const element = arguments[0];
                    const rect = element.getBoundingClientRect();
                    const x = rect.left + rect.width / 2;
                    const y = rect.top + rect.height / 2;
                    const topElement = document.elementFromPoint(x, y);
                    return topElement === element || element.contains(topElement);
                """, element)

                if not is_accessible:
                    return False

                element.click()
                return True

            except (
                ElementClickInterceptedException,
                StaleElementReferenceException,
            ):
                return False

        self.wait.until(
            click_when_available,
            message="Не удалось нажать на элемент: он недоступен или перекрыт"
        )

    # Получить текст элемента
    def get_text(self, locator):
        return self.find_element(locator).text

    # Проверить переход на указанный URL
    @allure.step("Проверить переход на страницу: {expected_url}")
    def is_url_opened(self, expected_url):
        try:
            return bool(
                self.wait.until(
                    lambda browser: (
                        browser.current_url.rstrip("/")
                        == expected_url.rstrip("/")
                    )
                )
            )
        except TimeoutException:
            return False

    # Перетащить элемент с помощью HTML5 Drag & Drop
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)

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

            dispatchDragEvent(source, "dragstart");
            dispatchDragEvent(target, "dragenter");
            dispatchDragEvent(target, "dragover");
            dispatchDragEvent(target, "drop");
            dispatchDragEvent(source, "dragend");
        """, source, target)
