from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys

class HomePage(BasePage):
    CLOSE_LOGIN = (By.CSS_SELECTOR, "button._2KpZ6l._2doB4z")
    SEARCH_BOX = (By.NAME, "q")

    def close_login_popup(self):
        self.click(self.CLOSE_LOGIN)

    def search_product(self, text):
        self.enter_text(self.SEARCH_BOX, text + Keys.ENTER)
