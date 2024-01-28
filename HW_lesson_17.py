import time

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from selenium import webdriver


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


def test_entrance(driver_chrome):
    driver_chrome.get('http://192.168.0.28:81/')
    login = driver_chrome.find_element(By.XPATH, '//body/form/div[2]/input')
    login.send_keys("admin")

    password = driver_chrome.find_element(By.XPATH, '//body/form/div[3]/div/input')
    password.send_keys("administrator")

    test_login = driver_chrome.find_element(By.XPATH, '//body/form/div[5]')
    test_login.click()

    result = driver_chrome.find_element(By.XPATH, '//body/div/div[3]/div/div/div[2]/h1')
    assert result.text == 'Hello, world!'


def test_url_documents(driver_chrome):
    driver_chrome.get('http://192.168.0.28:81/')
    login = driver_chrome.find_element(By.XPATH, '//body/form/div[2]/input')
    time.sleep(3)
    login.send_keys("admin")

    password = driver_chrome.find_element(By.XPATH, '//body/form/div[3]/div/input')
    password.send_keys("administrator")

    test_login = driver_chrome.find_element(By.XPATH, '//body/form/div[5]')
    test_login.click()
    time.sleep(2)

    magazines = driver_chrome.find_element(By.XPATH, '//label[2]/span')
    magazines.click()
    time.sleep(2)

    assert driver_chrome.current_url == 'http://192.168.0.28:81/orders/1'


def test_internal_documents(driver_chrome):
    driver_chrome.get('http://192.168.0.28:81/')
    login = driver_chrome.find_element(By.XPATH, '//body/form/div[2]/input')
    time.sleep(3)
    login.send_keys("admin")

    password = driver_chrome.find_element(By.XPATH, '//body/form/div[3]/div/input')
    password.send_keys("administrator")

    test_login = driver_chrome.find_element(By.XPATH, '//body/form/div[5]')
    test_login.click()
    time.sleep(2)

    magazines = driver_chrome.find_element(By.XPATH, '//label[2]/span')
    magazines.click()
    time.sleep(2)

    assert driver_chrome.current_url == 'http://192.168.0.28:81/orders/1'


def test_data_header(driver_chrome):
    driver_chrome.get('http://192.168.0.28:81/')
    login = driver_chrome.find_element(By.XPATH, '//body/form/div[2]/input')
    time.sleep(3)
    login.send_keys("admin")

    password = driver_chrome.find_element(By.XPATH, '//body/form/div[3]/div/input')
    password.send_keys("administrator")

    test_login = driver_chrome.find_element(By.XPATH, '//body/form/div[5]')
    test_login.click()
    time.sleep(2)

    magazines = driver_chrome.find_element(By.XPATH, '//label[2]/span')
    magazines.click()
    time.sleep(2)

    click_order = driver_chrome.find_element(By.XPATH, '//tbody/tr[51]')
    click_order.click()

    open_button = driver_chrome.find_element(By.XPATH, '//body/div[2]/div[1]/div/button[1]')
    open_button.click()
    time.sleep(5)

    xpath_text = '//*[text()= "Регистрационные данные"]'
    assert driver_chrome.find_element(By.XPATH, xpath_text)


def test_document_creating_folder(driver_chrome):
    driver_chrome.get('http://192.168.0.28:81/')
    login = driver_chrome.find_element(By.XPATH, '//body/form/div[2]/input')
    time.sleep(3)
    login.send_keys("admin")

    password = driver_chrome.find_element(By.XPATH, '//body/form/div[3]/div/input')
    password.send_keys("administrator")

    test_login = driver_chrome.find_element(By.XPATH, '//body/form/div[5]')
    test_login.click()
    time.sleep(2)

    magazines = driver_chrome.find_element(By.XPATH, '//label[2]/span')
    magazines.click()
    time.sleep(2)

    click_order = driver_chrome.find_element(By.XPATH, '//tbody/tr[51]')
    click_order.click()

    open_button = driver_chrome.find_element(By.XPATH, '//body/div[2]/div[1]/div/button[1]')
    open_button.click()
    time.sleep(5)

    create_folder_button = driver_chrome.find_element(By.XPATH, '//div[7]/button/span')
    create_folder_button.click()

    entering_folder_name = driver_chrome.find_element(By.XPATH, '//div[2]/div/span/input')
    entering_folder_name.send_keys("Новая папка")

    save_folder = driver_chrome.find_element(By.XPATH, '//div[3]/div[2]/div/div/button[1]')
    save_folder.click()
    time.sleep(3)

    name_folder = '//*[text()= "Новая папка"]'

    assert driver_chrome.find_element(By.XPATH, name_folder)
