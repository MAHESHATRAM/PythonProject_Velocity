from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)

driver.get('https://www.w3schools.com/')

element = driver.find_element(By.XPATH,"//h1[text()='Log in  ']")

time.sleep(2)

driver.execute_script('arguments[0].scrollIntoView();',element)
time.sleep(3)

#scroll to button of the page

driver.execute_script('window.scollBy(0,document.body.scrollHeight);')
time.sleep(3)

driver.execute_script('document.documentElement.scrollTop=0')
time.sleep(4)
