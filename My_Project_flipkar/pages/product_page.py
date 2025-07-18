from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
import time

class ProductPage(BasePage):

    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(),'Add to cart') or contains(text(),'GO TO CART')]")
    PRODUCT_NAME = (By.CLASS_NAME, 'B_NuCI')
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class,'_30jeq3') and contains(text(),'₹')]")
    CART_BTN_STATUS = (By.XPATH, "//button[contains(text(),'GOING TO CART')]")

    def get_product_name(self):
        self.wait_for_element(self.PRODUCT_NAME)
        return self.get_text(self.PRODUCT_NAME)

    def get_product_price(self):
        self.wait_for_element(self.PRODUCT_PRICE)
        return self.get_text(self.PRODUCT_PRICE)

    def add_to_cart(self):
        self.wait_for_element(self.ADD_TO_CART_BTN)
        self.click(self.ADD_TO_CART_BTN)
        self.wait_for_processing_to_finish()


    def verify_add_to_cart_text(self):
        self.wait_for_element(self.CART_BTN_STATUS)
        return self.get_text(self.CART_BTN_STATUS)
