from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#open facebook
# driver.implicitly_wait()
driver.get("https://www.w3schools.com/")

#scroll down by 4000 pixel varically

driver.execute_script('window.scrollBy(0,4000);')

#scrollup
time.sleep(2) 