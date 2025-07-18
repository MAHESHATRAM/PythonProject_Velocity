from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random
import string
import time

chrome_options = Options()
chrome_options.add_argument('--disable-notifications')

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.hdfcbank.com/")

time.sleep(10)

driver.quit()  # Don't forget the parentheses to actually quit the driver
