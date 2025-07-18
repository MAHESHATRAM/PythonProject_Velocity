from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#start chrome brower

driver  = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#Get wondow handle
driver.find_element(By.XPATH,"//a[contains(text(),'OrangeHRM, Inc')]").click();

time.sleep(3)

window_ids = driver.window_handles

print("Window IDs",window_ids) 

prent_window  = window_ids[0]
child_window  = window_ids[1]

driver.switch_to.window(child_window)

time.sleep(1)
print("Child window title :",driver.title)

time.sleep(2)

driver.switch_to.window(prent_window)

driver.find_element(By.NAME,'username').send_keys("Admin")
driver.find_element(By.NAME,'password').send_keys("admin123")
driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
time.sleep(2)
driver.quit()