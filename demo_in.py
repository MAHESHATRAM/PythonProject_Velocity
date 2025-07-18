# Click on Elements
# Get List of Items under Elements
# Select Text Box
# Enter details and submit the form
# Fetch the output generated post submission and verify
# https://demoqa.com  

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://demoqa.com")
catg_div = driver.find_element(By.CLASS_NAME,'card-up').click()
item = driver.find_element(By.CLASS_NAME,'text').click()
driver.find_element(By.XPATH,"//input[@placeholder='Full Name']").send_keys("MaheshAtram")
driver.find_element(By.ID,'userEmail').send_keys("mahesh@gamil.com")
currentadd = driver.find_element(By.XPATH,"//textarea[@placeholder='Current Address']").send_keys("Pune")
permantadd = driver.find_element(By.ID,'permanentAddress').send_keys("Nagpure")
driver.find_element(By.CSS_SELECTOR,'#submit').click()

# driver.find_element(By.ID,'submit').click()
# driver.find_element(By.CLASS_NAME,'btn btn-primary').click()
# print("Full Name", fullname,'\n',"Emails",emails,'\n',"Currentadd:",currentadd,"\n","permantadd:",permantadd)
fullname = driver.find_element(By.ID,'userName').text
emails =  driver.find_element(By.ID,'userEmail').text
currentadd = driver.find_element(By.ID,'currentadd').text
permantadd =driver.find_element(By.ID,'permanentAddress').text

assert "MaheshAtram" in fullname
assert "emails" in emails
assert "currentadd" in currentadd
assert "permantadd" in permantadd
output = driver.find_element(By.ID,"output").text
print(output)
time.sleep(5)
driver.close()