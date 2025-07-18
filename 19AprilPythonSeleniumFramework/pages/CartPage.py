from selenium.webdriver.common.by import By
from .BasePage import basePage

class CartPage(basePage):
    def check_product_in_cart(self, product_name):
        return self.is_visible((By.XPATH, f"//td[text()='{product_name}']"))

    def delete_product_from_cart(self, product_name):
        self.click((By.XPATH, f"//td[text()='{product_name}']/following-sibling::td/a[text()='Delete']"))

