from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.amazon.in/")

search_box = driver.find_element(By.ID,'twotabsearchtextbox')
search_box.send_keys("iphone 16pro max")

element = driver.find_element(By.XPATH,'')