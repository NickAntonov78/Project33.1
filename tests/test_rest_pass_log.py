import time
import pytest
from settings import valid_password3, valid_login
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


def test_rest_pass_log(driver):
    """Сценарий восстановления пароля по логину"""
    # Кликаем на кнопку забыл парполь
    driver.find_element(By.ID, 'forgot_password').click()
    # Кликаем на кнопку логин
    driver.find_element(By.ID, 't-btn-tab-login').click()
    # Вводим login
    driver.find_element(By.ID, 'username').send_keys(valid_login)
    time.sleep(15) # Таймер на ввод капчи
    # Кликаем на кнопку продолжить
    driver.find_element(By.ID, 'reset').click()
    time.sleep(2)
    # Кликаем на кнопку по номеру телефона
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div/label[1]/span/span[1]').click()
    # Кликаем на кнопку продолжить
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/button[1]').click()
    time.sleep(10) # Таймер на ввод sms cod
    # Вводим новый пароль
    driver.find_element(By.ID, 'password-new').send_keys(valid_password3)
    # Вводим новый пароль 2 раз
    driver.find_element(By.ID, 'password-confirm').send_keys(valid_password3)
    # Кликаем на кнопку сохранить
    driver.find_element(By.ID, 't-btn-reset-pass').click()
    # Проверяем что мы на странице авторизации и проверяем новый пароль в авторизации
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Авторизация'
    # Нажимаем на кнопку "Логин"
    driver.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(2)  # Ставим таймер на 2 сек для прогрузки контента страницы
    # Вводим логин УЗ
    driver.find_element(By.ID, 'username').send_keys(valid_login)
    time.sleep(2)  # Ставим таймер на 2 сек для прогрузки контента страницы
    # Вводим новый пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password3)
    time.sleep(2)  # Ставим таймер на 2 сек для прогрузки контента страницы
    # Нажимаем на кнопку "Войти"
    driver.find_element(By.ID, 'kc-login').click()
    time.sleep(2)  # Ставим таймер на 2 сек для прогрузки контента страницы
    # Проверяем что мы на странице ЛК
    assert driver.find_element(By.TAG_NAME, 'h3').text == "Учетные данные"


# pytest -v --driver Chrome --driver-path C:\\Users\\gelin\\PycharmProjects\\Project33.1\\webdriver\\chromedriver.exe test_rest_pass_log.py
