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

time.sleep(5)
driver.find_element(By.NAME,"firstname").send_keys("mahesh")
driver.find_element(By.NAME,"lastname").send_keys("Atram")
driver.find_element(By.NAME,"reg_email__").send_keys("Atram@gmail.com")
driver.find_element(By.ID,"password_step_input").send_keys("Atram@")

day=driver.find_element(By.ID,'day').click()
Month=driver.find_element(By.ID,'month').click()
Year=driver.find_element(By.ID,'year').click()

selectday = Select(day)
allday = selectday.options

print(f"total number of day options :",{len(allday)})



