import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

driver.get(By.XPATH,"//input[@type='text' or @placeholder='First Name']").send_keys("Mahesh")
driver.get(By.XPATH,"//input[@type='text' or @ng-model='LastName']").send_keys('Major')