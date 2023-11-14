import time
import pytest
from settings import valid_password, valid_pnumbery
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


def test_authorization_ya_id(driver):
    """ Проверяем авторизацию через соц сеть яндекс id """
    # Кликаем на кнопку яндекс id
    driver.find_element(By.ID, 'oidc_ya').click()
    time.sleep(1)
    driver.find_element(By.ID, 'oidc_ya').click() # Кликаем на кнопку яндекс id 2 раз что-бы обойти баг №1
    time.sleep(2) # Ставим таймер на 2 сек для прогрузки контента страницы
    # Вводим телефон учетной записи
    driver.find_element(By.ID, 'passp-field-phone').send_keys(valid_pnumbery)
    # Вводим пароль учетной записи
    driver.find_element(By.ID, 'passp:phone:controls:next').click()
    time.sleep(20) # Ставим таймер на 20 сек что-бы успеть ввести код из смс вручную
    # Кликаем на кнопку с данными аккаунта яндекс id для подтверждения входа
    driver.find_element(By.XPATH, '//*[@id="accounts:item-146079957"]').click()
    time.sleep(5) # Ставим таймер на 5 сек для прогрузки контента страницы
    # Проверяем что мы на странице ЛК
    assert driver.find_element(By.TAG_NAME, 'h3').text == "Учетные данные"




# pytest -v --driver Chrome --driver-path C:\\Users\\gelin\\PycharmProjects\\Project33.1\\webdriver\\chromedriver.exe test_authorization_ya_id.py