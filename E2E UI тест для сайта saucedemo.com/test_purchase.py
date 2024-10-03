import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    """Инициализация драйвера перед каждым тестом"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)  # Устанавливаем неявное ожидание
    yield driver  # Возвращаем драйвер для использования в тесте
    driver.quit()  # Закрываем браузер после завершения теста

def test_purchase(driver):
    """Тест на покупку товара на сайте saucedemo.com"""
    # Открываем сайт
    driver.get("https://www.saucedemo.com")

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Выбор товара и добавление его в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

    # Проверка, что товар добавлен
    assert driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"

    # Переход к оформлению заказа
    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

    # Заполнение полей с информацией для заказа
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    time.sleep(3)

    # Завершение покупки
    driver.find_element(By.ID, "finish").click()

    # Проверка успешного завершения покупки
    success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert success_message == "THANK YOU FOR YOUR ORDER"
