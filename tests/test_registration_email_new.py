import time
import pytest
from settings import valid_password, valid_emailtwo, sname, name
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


def test_registration_email_new(driver):
    """Сценарий регистрации с новой почтой"""
    # Кликаем на кнопку зарегистрироваться
    driver.find_element(By.ID, 'kc-register').click()
    # Ставим таймер на 2 сек для прогрузки контента страницы
    time.sleep(2)
    # Вводим имя
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input').send_keys(name)
    # Вводим фамилию
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input').send_keys(sname)
    # Вводим почту
    driver.find_element(By.ID, 'address').send_keys(valid_emailtwo)
    # Вводим пароль
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    # Вводим подтверждение пароля
    driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    # Кликаем на кнопку продолжить
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button').click()
    time.sleep(20) # Таймер 20 секунд что-бы успеть ввести код с почты
    # Проверяем что мы на странице ЛК
    assert driver.find_element(By.TAG_NAME, 'h3').text == "Учетные данные"



# pytest -v --driver Chrome --driver-path C:\\Users\\gelin\\PycharmProjects\\Project33.1\\webdriver\\chromedriver.exe test_registration_email_new.py