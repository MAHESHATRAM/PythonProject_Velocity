from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class CartPage(BasePage):

    TOTAL_AMOUNT = (By.XPATH, "//span[contains(text(),'Total Amount')]/following-sibling::span")
    INCREASE_QTY_BTN = (By.XPATH, "//button[text()='+']")
    QTY_CHANGED_POPUP = (By.XPATH, "//div[contains(text(),'QUANTITY to')]")
    REMOVE_LINK = (By.XPATH, "//div[text()='Remove']")
    CONFIRM_REMOVE_BTN = (By.XPATH, "//div[@class='_3dsJAO _24d-qY FhkMJZ']")
    REMOVE_MSG = (By.XPATH, "//div[contains(text(),'from your cart')]")
    EMPTY_CART_MSG = (By.XPATH, "//div[contains(text(),'Missing Cart items?')]")

    def verify_total_amount(self, expected_price):
        self.wait_for_element(self.TOTAL_AMOUNT)
        actual_price = self.get_text(self.TOTAL_AMOUNT)
        assert actual_price == expected_price, f"Expected: {expected_price}, Got: {actual_price}"

    def increase_quantity(self):
        self.wait_for_element(self.INCREASE_QTY_BTN)
        self.click(self.INCREASE_QTY_BTN)
        time.sleep(2)  # wait for popup to appear

    def get_qty_popup_text(self):
        self.wait_for_element(self.QTY_CHANGED_POPUP)
        return self.get_text(self.QTY_CHANGED_POPUP)

    def remove_item(self):
        self.wait_for_element(self.REMOVE_LINK)
        self.click(self.REMOVE_LINK)
        time.sleep(1)

    def confirm_remove(self):
        self.wait_for_element(self.CONFIRM_REMOVE_BTN)
        self.click(self.CONFIRM_REMOVE_BTN)
        time.sleep(2)

    def get_remove_confirmation_text(self):
        self.wait_for_element(self.REMOVE_MSG)
        return self.get_text(self.REMOVE_MSG)

    def is_cart_empty_message_displayed(self):
        self.wait_for_element(self.EMPTY_CART_MSG)
        return self.driver.find_element(*self.EMPTY_CART_MSG).is_displayed()
