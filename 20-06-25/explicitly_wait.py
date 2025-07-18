from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver =webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://www.facebook.com/")



email = driver.find_elements(By.ID,'email').send_keys('Mahesh')
pass1 = driver.find_element(By.ID,'pass').send_keys('pass')
pass1.send_keys('kalk')

click = driver.find_element(By.NAME,'login').click()

driver.quit()

