from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#open facebook
# driver.implicitly_wait()
driver.get("https://www.facebook.com/")
input1=driver.find_element(By.ID,"email")
input2 = driver.find_element(By.ID,"pass")

login_button = driver.find_element(By.XPATH,'//button[@name="login"]')

#use javascript execut to set value and click

driver.execute_script("arguments[0].value = 'test@gmail.com';",input1)
driver.execute_script("arguments[0].value = 'test@123';",input2)
driver.execute_script("arguments[0].click();",login_button)
time.sleep(2)