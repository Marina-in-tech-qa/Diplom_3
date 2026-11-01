
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
)


class BasePage:

    # Инициализировать драйвер и ожидание элементов
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Открыть страницу по указанному адресу
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

                    return topElement === element ||
                           element.contains(topElement);
                """, element)

                if not is_accessible:
                    return False

                # Нажать на элемент через Selenium
                element.click()
                return True

            except (
                ElementClickInterceptedException,
                StaleElementReferenceException,
            ):
                return False

        # Дождаться успешного нажатия
        self.wait.until(
            click_when_available,
            message="Не удалось нажать на элемент: он недоступен или перекрыт"
        )

    # Получить текст элемента
    def get_text(self, locator):
        return self.find_element(locator).text
