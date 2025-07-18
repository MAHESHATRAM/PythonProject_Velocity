from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.support.ui import WebDriverWait

import time
from .base_page import BasePage
class CartPage(BasePage):
    def wait_for_cart(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Price details']")))

    def get_total_amount(self):
        amount_text = self.driver.find_element(
            By.XPATH, "//div[@class='_1Y9Lgu']/descendant-or-self::div"
        ).text.strip()
        return amount_text

    def clean_price(self, price_text):
        """
        Cleans a price string (e.g., '₹14,999') and converts it to an integer.
        :param price_text: Raw price string
        :return: Integer price or None if conversion fails
        """
        if not price_text:
            return None  # or raise ValueError("Price text is empty")

        numeric_string = re.sub(r"[^\d]", "", price_text)
        
        if not numeric_string:
            return None  # or raise ValueError("No digits found in price text")

        return int(numeric_string)
    def get_platform_fee(self):
        """
        Gets the platform fee (Protect Promise Fee) from the cart summary.
        :return: Platform fee text (e.g., '₹99')
        """
        fee_text = self.driver.find_element(
            By.XPATH, "//div[@class='_59Raj+']//child::div[text()='Protect Promise Fee']/descendant-or-self::div"
        ).text.strip()
        return fee_text

    def increase_quantity(self):
        plus_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='atHedL']//following-sibling::button[text()='+']")))
        plus_btn.click()
        msg = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'QUANTITY to')]")))
        return msg.text

    def remove_product(self):
        remove_btns = self.driver.find_elements(By.XPATH, "//div[text()='Remove']")
        if remove_btns:
            remove_btns[0].click()
            print("✅ First 'Remove' button clicked.")
        else:
            print("❌ No 'Remove' button found.")
        
        dialog = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='container']//child::div//child::div//child::div//child::button[text()='✕']")))
        assert self.driver.find_element(By.XPATH, "//div[text()='Cancel']")
        confirm = self.driver.find_element(By.XPATH, "//div[text()='Remove']")
        confirm.click()

    def verify_empty_cart(self):
        msg1 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Missing Cart items?']")))
        msg2 = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[text()='Login to see the items you added previously']")))
        return msg1.is_displayed() and msg2.is_displayed()
    