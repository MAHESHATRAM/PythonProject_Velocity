from selenium.webdriver.common.by import By
from .BasePage import basePage


class LoginPage(basePage):

    LOGIN_LINK = (By.ID, "login2")
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_BTN = (By.XPATH, "//button[contains(text(),'Log in')]")
    LOGIN_CANCEL =(By.XPATH,"//button[contains(text(),'Log in')]//preceding-sibling::button[text()='Close']")
    WELCOME_USER = (By.ID, "nameofuser")  # Assuming success shows this


    def open_login_modal(self):
        self.click(self.LOGIN_LINK)

    def open_login_cancel(self):
        self.click(self.LOGIN_CANCEL)

    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)

    def is_login_successful(self):
        return self.is_visible(self.WELCOME_USER)
