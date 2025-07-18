from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.google.co.in/")

time.sleep(3)
driver.save_screenshot("Google_homepage.png")

#alternative method

driver.get_screenshot_as_file("Demo.png")

driver.quit()