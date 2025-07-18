# //input[@class="inputtext _55r1 _6luy"]
# //a[@data-testid="open-registration-form-button"]
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
import time
from selenium.webdriver.common.by import By

#open facebook
excepted_title = "Facebook – log in or sign up"
driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH,"//input[@class='inputtext _55r1 _6luy']").send_keys("maheshatram@gmail.com")
# time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("Mahesh@2420")#xpath by attribute
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
driver.close()