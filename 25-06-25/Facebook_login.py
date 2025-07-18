from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver



class FacebookLoginPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.userName =  (By.ID, 'email')
        self.password =  (By.ID,'pass')
        self.loginButton = (By.NAME, 'login')
        self.createAccount = (By.XPATH, "//a[contains(text(),'Create new account')]")
        self.facebookLogo = (By.XPATH,'//img[@class="fb_logo _8ilh img"]')

    def enter_username(self, username):
        self.driver.find_element(*self.userName).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(*self.loginButton).click()

    def click_create_account(self):
        self.driver.find_element(*self.createAccount).click()
    
    def check_logo(self):
        logo = self.driver.find_element(*self.facebookLogo)
        if logo.is_displayed():
            print("logo displayed")
        else:
            print("logo not displayed")