from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

driver.find_element(By.NAME , 'username').send_keys("Admin")
driver.find_element(By.NAME,'password').send_keys('admin123')

driver.find_element(By.XPATH,'//button[@type="submit"]').click();

time.sleep(3)

text =driver.find_element(By.XPATH,'//h6[contains(@class,"oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module")]').text

if text == "Dashboard1":
    print("Login Successfully")
else:
    print("Incorrect dashobard name")