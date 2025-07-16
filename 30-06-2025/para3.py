from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("standard_user", "secret_sauce"),
    ("standard_user1", "secret_sauce")
])
def test_login(browser, username, password):
    browser.get("https://www.saucedemo.com/v1/")
    browser.find_element(By.ID, 'user-name').send_keys(username)
    browser.find_element(By.ID, 'password').send_keys(password)
    browser.find_element(By.ID, 'login-button').click()
    