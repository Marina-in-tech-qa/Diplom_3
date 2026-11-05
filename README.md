# Diplom_3 — UI-тестирование Stellar Burgers

Третья часть дипломного проекта Яндекс Практикума по автоматизации тестирования.

## О проекте

Автоматизированные UI-тесты веб-приложения Stellar Burgers.

Сайт: https://qa-stellarburgers.education-services.ru

Тестирование выполняется в двух браузерах:
- Google Chrome
- Mozilla Firefox

## Технологии

- Python
- Selenium WebDriver
- Pytest
- Page Object Model
- Allure Framework
- Requests

## Структура проекта

- `pages/` — классы Page Object
- `locators/` — локаторы элементов
- `tests/` — автоматизированные тесты
- `conftest.py` — фикстуры Pytest
- `helpers.py` — вспомогательные функции
- `urls.py` — адреса страниц и API
- `requirements.txt` — зависимости проекта

## Проверяемая функциональность

1. Авторизация пользователя.
2. Переход между конструктором и лентой заказов.
3. Открытие и закрытие модального окна ингредиента.
4. Добавление ингредиента в конструктор и проверка счётчика.
5. Увеличение общего количества заказов.
6. Увеличение количества заказов за сегодня.
7. Отображение оформленного заказа в разделе «В работе».

## Установка зависимостей

```bash
pip install -r requirements.txt
```

Для запуска тестов необходимо установить Google Chrome и Mozilla Firefox, а также обеспечить доступность соответствующих WebDriver.

## Запуск тестов

```bash
python -m pytest tests/ -v
```

## Запуск с Allure

```bash
python -m pytest tests/ --alluredir=allure_results
```

Просмотр отчёта:

```bash
allure serve allure_results
```

Для просмотра отчёта необходим установленный Allure Commandline.

## Результаты

Реализовано 9 параметризованных тестов, выполняемых в Chrome и Firefox.

Успешный локальный прогон: **18 passed**.
