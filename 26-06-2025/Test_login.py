from selenium import webdriver
from Facebook_login import FacebookLoginPage
from FacebookCreateaccount import FacebookCreateaccount
import time
import json

with open('V:\Velocity_Python_Automation_testing\Automation\Python_Selenium\TestData\FtestData.json','r') as f:
    data = json.load(f)

url =  data["url"]
# username =  data["login"]["username"]
# password =  data["login"]["password"]
# firstname = data["signup"]["firstname"]
# lastname  = data["signup"]["lastname"]
# signup_email  = data["signup"]["email"]
# signup_pwd = data["signup"]["password"]
username = data["login"]["username"]
password = data["login"]["password"]
firstname = data["signup"]["firstname"]
lastname = data["signup"]["lastname"]
signup_email = data["signup"]["email"]
signup_pwd = data["signup"]["password"]




 #step 1
 
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get(url)

#step 2 - login actions
login_page = FacebookLoginPage(driver)
# login_page.enter_username(username)
# login_page.enter_password(password)
# login_page.check_logo()
# login_page.click_login()

# time.sleep(4)
#step 2 - go the create account
login_page.click_create_account()
signup_page = FacebookCreateaccount(driver)

signup_page.enter_firstname(firstname)
signup_page.enter_lastname(lastname)
signup_page.select_dob(data["signup"]["dob"]["day"],
                       data["signup"]["dob"]["month"],
                       data["signup"]["dob"]["year"]
                       )
signup_page.click_gender()
signup_page.enter_email(signup_email)
signup_page.enter_password(signup_pwd)
test =signup_page.clcik_signup()
time.sleep(4)


