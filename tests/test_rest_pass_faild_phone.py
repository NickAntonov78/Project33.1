import time
import pytest
from settings import valid_pnumber
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome('C:\\Users\\gelin\\PycharmProjects\\Project33.1\\webdriver\\chromedriver.exe')
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=5206c328-fecf-4f55-9e44-bd825fd27487&theme=light&auth_type')
    time.sleep(2) # Ставим таймер на 2 сек для прогрузки контента страницы
    driver.maximize_window()
    time.sleep(2) # Ставим таймер на 2 сек для прогрузки контента страницы
    yield driver
    driver.quit()


def test_rest_pass_faild_phone(driver):
    """Сценарий восстановления пароля по телефону при рандомных символах в капче"""
    # Кликаем на кнопку забыл парполь
    driver.find_element(By.ID, 'forgot_password').click()
    # Вводим телефон
    driver.find_element(By.ID, 'username').send_keys(valid_pnumber)
    # Вводим рандомные символы в капчу
    driver.find_element(By.ID, 'captcha').send_keys('QwErTy12')
    # Кликаем на кнопку продолжить
    driver.find_element(By.ID, 'reset').click()
    # Проверяем тест на корректность сообщением неверный логин или текст с картинки
    assert driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или текст с картинки'



# pytest -v --driver Chrome --driver-path C:\\Users\\gelin\\PycharmProjects\\Project33.1\\webdriver\\chromedriver.exe test_rest_pass_faild_phone.py