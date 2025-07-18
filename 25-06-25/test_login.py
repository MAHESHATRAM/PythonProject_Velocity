from selenium import webdriver
from Facebook_login import FacebookLoginPage
from FacebookCreateaccount import FacebookCreateaccount

import time
#step 1
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.facebook.com/")

#step 2 - login actions
login_page = FacebookLoginPage(driver)
# login_page.enter_username('Test@gmail.com')
# login_page.enter_password("demo123")
# login_page.check_logo()
# login_page.click_login()

time.sleep(4)
#step 2 - go the create account
login_page.click_create_account()
signup_page = FacebookCreateaccount(driver)

signup_page.enter_firstname("Rohit")
signup_page.enter_lastname("Test")
signup_page.click_gender()
signup_page.enter_email("Test@gmailc.om")
signup_page.enter_password("345678i")
test =signup_page.clcik_signup()

time.sleep(4)


