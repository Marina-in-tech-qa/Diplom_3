
import allure

from pages.login_page import LoginPage
from urls import BASE_URL


@allure.feature("Авторизация")
class TestLogin:

    # Проверить успешный вход зарегистрированного пользователя
    @allure.title("Успешный вход зарегистрированного пользователя")
    def test_login_success(self, driver, created_user):
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
            assert page.is_login_successful()
