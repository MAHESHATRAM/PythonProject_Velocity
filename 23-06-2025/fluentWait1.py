from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def fluent_wait_for_element(driver,timeout,locator,poll_frequency):
    wait = WebDriverWait(driver,timeout=timeout,poll_frequency=poll_frequency,ignored_exceptions=[NoSuchElementException])
    return wait.until(lambda d:d.find_element(*locator))

driver =webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(5)

driver.get("https://www.facebook.com/")

username = (By.ID,'email')
password = (By.ID,'pass')
fluent_wait_for_element(driver,10,username).send_key
