from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver =webdriver.Chrome()

driver.get("https://www.facebook.com/")

all_links = driver.find_elements(By.TAG_NAME,'a')

print(f"Toatl Link: ,{len(all_links)}")
for link in all_links:
    print("Link : ",link.text)
    print('Href',link.get_attribute('href'))
    # print()