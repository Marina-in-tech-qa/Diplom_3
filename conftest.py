
import pytest
import requests

from selenium import webdriver

from helpers import generate_user_data
from urls import CREATE_USER_URL, DELETE_USER_URL


# Запустить браузер Chrome или Firefox для теста
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()

    browser.maximize_window()

    yield browser

    browser.quit()


# Создать тестового пользователя и удалить его после теста
@pytest.fixture
def created_user():
    user_data = generate_user_data()

    # Зарегистрировать тестового пользователя через API
    response = requests.post(
        CREATE_USER_URL,
        json=user_data,
        timeout=10
    )

    # Проверить успешность подготовки тестовых данных
    if response.status_code != 200:
        pytest.fail(
            f"Не удалось создать тестового пользователя. "
            f"Статус: {response.status_code}. "
            f"Ответ сервера: {response.text}"
        )

    access_token = response.json()["accessToken"]

    try:
        yield user_data

    finally:
        # Удалить тестового пользователя после выполнения теста
        requests.delete(
            DELETE_USER_URL,
            headers={"Authorization": access_token},
            timeout=10
        )
