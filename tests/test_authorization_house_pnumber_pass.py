import time
import pytest
from settings import valid_password, valid_pnumber
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def pdriver():
    pdriver = webdriver.Chrome('C:\\Users\\gelin\\PycharmProjects\\Project33.1\\webdriver\\chromedriver.exe')
    pdriver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_smarthome&response_type=code&scope=openid&redirect_uri=https%3A%2F%2Flk.smarthome.rt.ru%2Foauth2%2Fcallback')
    time.sleep(2) # Ставим таймер на 2 сек для прогрузки контента страницы
    pdriver.maximize_window()
    time.sleep(2) # Ставим таймер на 2 сек для прогрузки контента страницы
    yield pdriver
    pdriver.quit()


def test_authorization_house_pnumber_pass(pdriver):
    """Сценарий авторизации через телефон и пароль на сайте Умный дом"""
    # Кликаем на кнопку пойти с паролем
    pdriver.find_element(By.ID, 'standard_auth_btn').click()
    time.sleep(2)
    # Вводим почту
    pdriver.find_element(By.ID, 'username').send_keys(valid_pnumber)
    # Вводим пароль
    pdriver.find_element(By.ID, 'password').send_keys(valid_password)
    # Кликаем на кнопку войти
    pdriver.find_element(By.ID, 'kc-login').click()
    time.sleep(5)
    # проверяем что мы на домашнем экране
    assert pdriver.find_element(By.TAG_NAME, 'h2').text == 'Это домашний экран'



# pytest -v --driver Chrome --driver-path C:\\Users\\gelin\\PycharmProjects\\Project33.1\\webdriver\\chromedriver.exe test_authorization_house_pnumber_pass.py