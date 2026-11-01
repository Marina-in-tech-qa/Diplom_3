
import allure

from pages.login_page import LoginPage
from urls import BASE_URL


@allure.feature("Авторизация")
@allure.title("Успешный вход зарегистрированного пользователя")
def test_login_success(driver, created_user):
    page = LoginPage(driver)

    # Открыть страницу входа
    with allure.step("Открыть страницу авторизации"):
        page.open(f"{BASE_URL}/login")

    # Авторизоваться под созданным пользователем
    with allure.step("Войти под тестовым пользователем"):
        page.login(
            created_user["email"],
            created_user["password"]
        )

    # Проверить успешную авторизацию
    with allure.step("Проверить переход на главную страницу"):
        page.wait.until(
            lambda browser: browser.current_url.rstrip("/")
            == BASE_URL
        )

        assert driver.current_url.rstrip("/") == BASE_URL
    