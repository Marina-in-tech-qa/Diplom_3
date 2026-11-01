
from selenium.webdriver.common.by import By


class LoginLocators:

    # Поле ввода электронной почты
    EMAIL_INPUT = (
        By.NAME,
        "name"
    )

    # Поле ввода пароля
    PASSWORD_INPUT = (
        By.NAME,
        "Пароль"
    )

    # Кнопка «Войти» на странице авторизации
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Войти']"
    )
