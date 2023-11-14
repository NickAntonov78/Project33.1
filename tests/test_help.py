import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome('../webdriver/chromedriver.exe')
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=5206c328-fecf-4f55-9e44-bd825fd27487&theme=light&auth_type')
    time.sleep(2) # Ставим таймер на 2 сек для прогрузки контента страницы
    driver.maximize_window()
    time.sleep(2) # Ставим таймер на 2 сек для прогрузки контента страницы
    yield driver
    driver.quit()


def test_help(driver):
    """Проверка страницы помощь на кликабельность спойлеров"""
    # Кликаем на кнопку помощь
    driver.find_element(By.ID, 'faq-open').click()
    time.sleep(2)
    # Открываем спойлер 1
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/div/div/div[2]/div[1]/div[1]').click()
    time.sleep(2)
    # Открываем спойлер 2
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/div/div/div[2]/div[2]/div').click()
    time.sleep(2)
    # Открываем спойлер 3
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/div/div/div[2]/div[3]/div').click()
    time.sleep(2)
    # Открываем спойлер 4
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/div/div/div[2]/div[4]/div[1]').click()
    time.sleep(2)
    # Открываем спойлер 5
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/div/div/div[2]/div[5]/div[1]/h2').click()
    time.sleep(2)
    # Открываем спойлер 6
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/div/div/div[2]/div[6]/div').click()
    time.sleep(2)
    # Открываем спойлер 7
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/div/div/div[2]/div[7]/div/h2').click()
    time.sleep(2)
    # Открываем спойлер 8
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/div/div/div[2]/div[8]/div').click()
    time.sleep(2)
    # Открываем спойлер 9
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/div/div/div[2]/div[9]/div').click()
    time.sleep(2)

# pytest -v --driver Chrome --driver-path C:\\Users\\gelin\\PycharmProjects\\Project33.1\\webdriver\\chromedriver.exe test_help.py
