from selenium import webdriver
from selenium.webdriver.common.by import By

import random
import string
import time

def generate_random_string():
    length = 8
    return ''.join(random.choice(string.ascii_letters+string.digits))


driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.facebook.com/")

facbook_logo = driver.find_element(By.XPATH,"//img[@class='fb_logo _agiv img']")

imag_name = 'googlepage'
random_suffix = generate_random_string()

screenshot_filename = f"{imag_name}_{random_suffix}.png"

save_path = f"V:\Velocity_Python_Automation_testing\Automation\Python_Selenium\Screenshots\{screenshot_filename}"

driver.save_screenshot(save_path)
time.sleep(5)
driver.quit()