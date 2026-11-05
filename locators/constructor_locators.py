
from selenium.webdriver.common.by import By


class ConstructorLocators:

    # Кнопка «Конструктор» в шапке сайта
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[text()='Конструктор']"
    )

    # Кнопка «Лента заказов» в шапке сайта
    ORDER_FEED_BUTTON = (
        By.XPATH,
        "//p[text()='Лента Заказов']"
    )

    # Перетаскиваемая карточка булки
    INGREDIENT_CARD = (
        By.XPATH,
        "//a[@draggable='true'][.//p[text()='Флюоресцентная булка R2-D3']]"
    )

    # Заголовок модального окна ингредиента
    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        "//h2[text()='Детали ингредиента']"
    )

    # Кнопка закрытия модального окна
    INGREDIENT_MODAL_CLOSE = (
        By.CSS_SELECTOR,
        "section[class*='Modal_modal_opened'] button[class*='Modal_modal__close__']"
    )

    # Счётчик булки «Флюоресцентная булка R2-D3»
    INGREDIENT_COUNTER = (
        By.XPATH,
        "//a[.//p[text()='Флюоресцентная булка R2-D3']]"
        "//p[contains(@class, 'counter_counter__num')]"
    )

    # Область корзины для перетаскивания ингредиента
    BURGER_BASKET = (
        By.CSS_SELECTOR,
        "ul[class*='BurgerConstructor_basket__list']"
    )

    # Кнопка «Оформить заказ»
    ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Оформить заказ']"
    )

    # Номер оформленного заказа в модальном окне
    ORDER_NUMBER = (
        By.CSS_SELECTOR,
        "section[class*='Modal_modal_opened'] h2.text_type_digits-large"
    )
