
import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from urls import BASE_URL


class LoginPage(BasePage):

    # Авторизоваться с помощью email и пароля
    @allure.step("Авторизоваться под тестовым пользователем")
    def login(self, email, password):
        self.find_element(
            LoginLocators.EMAIL_INPUT
        ).send_keys(email)

        self.find_element(
            LoginLocators.PASSWORD_INPUT
        ).send_keys(password)

        self.click_element(
            LoginLocators.LOGIN_BUTTON
        )

    # Проверить успешную авторизацию по переходу на главную страницу
    @allure.step("Проверить успешный переход на главную страницу")
    def is_login_successful(self):
        try:
            return self.wait.until(
                EC.url_to_be(BASE_URL + "/")
            )
        except TimeoutException:
            return False
