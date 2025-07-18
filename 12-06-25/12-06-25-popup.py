from selenium import webdriver
from selenium.webdriver.common.by import By

import random
import string
import time

# def generate_random_string():
#     length = 8
#     return ''.join(random.choice(string.ascii_letters+string.digits))


driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()

#validate the result text

expt_txt = 'You successfully clicked an alert'
actual_txt = 'You successfully clicked an alert'
# assert "You successfully clicked an alert" in expt_txt
if expt_txt in actual_txt:
    print("Correct Text")
else:
    print("Incorrect Text")

