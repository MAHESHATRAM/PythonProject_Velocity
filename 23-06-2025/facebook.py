from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json


#step1 load single crede ser from json

with open("V:\Velocity_Python_Automation_testing\Automation\Python_Selenium\TestData\FacebookLoginData.json","r") as file:
    credentuals= json.load(file)
    
driver =webdriver.Chrome()


for account_name, creads in credentuals["Account1"].items():
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    
    driver.find_element(By.ID,"email").clear()
    driver.find_element(By.ID,"email").send_keys(creads["email"])
    driver.find_element(By.ID,"pass").clear()
    driver.find_element(By.ID,"emial").send_keys(creads["pass"])
    
    