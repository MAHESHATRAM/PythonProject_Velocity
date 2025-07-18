from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import json

with open("V:\Velocity_Python_Automation_testing\Automation\Python_Selenium\TestData\LoginData.json","r") as file:
    data = json.load(file)
    
username = data['username']
password = data['Password']
data = data['Dashbord']
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

driver.find_element(By.NAME,'username').send_keys(username)
driver.find_element(By.NAME,'Password').send_keys(password)

driver.find_element(By.XPATH,"//button[@type='submit']").click()


