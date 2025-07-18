from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def select_dropdown_by_text(element,text):
    select = Select(element)
    select.select_by_visible_text(text)
driver = webdriver.Chrome()
    
    
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH,"//a[text()='Create new account']").click()

day=driver.find_element(By.XPATH,"//select[aria-label='Day']").click()
Month=driver.find_element(By.XPATH,"//select[aria-label='Month']").click()
Year=driver.find_element(By.XPATH,"//select[aria-label='Year']").click()
#Select_by_index
Select(day).select_by_index(3)
Select(Month).select_by_index(3)
Select(Year).select_by_index(3)

date_string = "22/2/2023"
date_part = date_string.split("/")



