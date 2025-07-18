from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.amazon.in/")

search_box = driver.find_element(By.ID,'twotabsearchtextbox')
search_box.send_keys("iphone")

element = driver.find_elements(By.XPATH,'//div[@class="s-suggestion s-suggestion-ellipsis-direction"]')
for i in element:
    print("Product is : ",i.text)
    
print("Correct way")

time.sleep(4)
driver.quit()