import time
import pytest
from settings import valid_password, valid_pnumber
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


def test_authorization_pnumber_pass(driver):
    """Проверяем стандартную авторизацю по почте и паролю"""

    # Вводим телефон УЗ
    driver.find_element(By.ID, 'username').send_keys(valid_pnumber)
    time.sleep(2) # Ставим таймер на 2 сек для прогрузки контента страницы
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    time.sleep(2) # Ставим таймер на 2 сек для прогрузки контента страницы
    # Нажимаем на кнопку "Войти"
    driver.find_element(By.ID, 'kc-login').click()
    time.sleep(2) # Ставим таймер на 2 сек для прогрузки контента страницы
    # Проверяем что мы на странице ЛК
    assert driver.find_element(By.TAG_NAME, 'h3').text == "Учетные данные"


# pytest -v --driver Chrome --driver-path C:\\Users\\gelin\\PycharmProjects\\Project33.1\\webdriver\\chromedriver.exe test_authorization_pnumber_pass.py