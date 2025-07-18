from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver =webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(5)

driver.get("https://www.facebook.com/")

wait = WebDriverWait