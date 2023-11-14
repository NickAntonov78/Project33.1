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


def test_authorization_ok(driver):
    """ Проверяем авторизацию через соц сеть однокласники """
    # Кликаем на кнопку OK
    driver.find_element(By.ID, 'oidc_ok').click()
    time.sleep(2) # Ставим таймер на 2 сек для прогрузки контента страницы
    # Вводим телефон учетной записи
    driver.find_element(By.ID, 'field_email').send_keys(valid_pnumber)
    # Вводим пароль учетной записи
    driver.find_element(By.ID, 'field_password').send_keys(valid_password)
    # Кликаем на кнопку войти
    driver.find_element(By.XPATH, '//*[@id="widget-el"]/div[2]/div/div/div[4]/input').click()
    time.sleep(5) # Ставим таймер на 5 сек для прогрузки контента страницы
    # Проверяем что мы на странице ЛК
    assert driver.find_element(By.TAG_NAME, 'h3').text == "Учетные данные"



# pytest -v --driver Chrome --driver-path C:\\Users\\gelin\\PycharmProjects\\Project33.1\\webdriver\\chromedriver.exe test_authorization_ok.py