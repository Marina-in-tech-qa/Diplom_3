
import allure

from pages.base_page import BasePage
from locators.login_locators import LoginLocators


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
