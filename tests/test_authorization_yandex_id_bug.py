import time
import pytest
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


def test_authorization_yandex_id_bug(driver):
    """ Проверяем авторизацию через соц сеть яндекс id """
    # Кликаем на кнопку яндекс id
    driver.find_element(By.ID, 'oidc_ya').click()
    time.sleep(2) # Ставим таймер на 2 сек для прогрузки контента страницы
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Введите номер телефона для создания Яндекс ID"
    # Баг. Страница с авторизацией яндекс id не открывается с 1 клика по иконке яндекс id

# pytest -v --driver Chrome --driver-path C:\\Users\\gelin\\PycharmProjects\\Project33.1\\webdriver\\chromedriver.exe test_authorization_yandex_id_bug.py