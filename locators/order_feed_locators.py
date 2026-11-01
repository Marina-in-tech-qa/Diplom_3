
from selenium.webdriver.common.by import By


class OrderFeedLocators:

    # Счётчик выполненных заказов за всё время
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p"
    )

    # Счётчик выполненных заказов за сегодня
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p"
    )

    # Список номеров заказов в разделе «В работе»
    IN_PROGRESS_ORDERS = (
        By.XPATH,
        "//p[text()='В работе:']/following-sibling::ul"
    )
