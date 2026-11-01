
import pytest
import requests
from selenium import webdriver

from helpers import generate_user_data
from urls import CREATE_USER_URL, DELETE_USER_URL


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()

    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.fixture
def created_user():
    user_data = generate_user_data()

    response = requests.post(
        CREATE_USER_URL,
        json=user_data,
        timeout=10
    )

    assert response.status_code == 200

    access_token = response.json()["accessToken"]

    try:
        yield user_data
    finally:
        requests.delete(
            DELETE_USER_URL,
            headers={"Authorization": access_token},
            timeout=10
        )

