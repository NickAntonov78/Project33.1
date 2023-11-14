import time
import pytest
from settings import valid_pnumber
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


def test_authorization_house_kod(pdriver):
    """Сценарий авторизации по одноразовому коду (телефон)"""
    # Вводим телефон УЗ
    pdriver.find_element(By.ID, 'address').send_keys(valid_pnumber)
    # Кликаем на кнопку получить код
    pdriver.find_element(By.ID, 'otp_get_code').click()
    time.sleep(20) # Таймер 20 секунд что-бы успеть ввести код с sms
    # Проверяем что мы на домашнем экране
    assert pdriver.find_element(By.TAG_NAME, 'h2').text == 'Это домашний экран'



# pytest -v --driver Chrome --driver-path C:\\Users\\gelin\\PycharmProjects\\Project33.1\\webdriver\\chromedriver.exe test_authorization_house_kod.py
