from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from .base_page import BasePage

class ProductPage(BasePage):
    def switch_to_product_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_product_title(self):
        elem = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[@class='VU-ZEz'] | //span[@class='B_NuCI']")))
        return elem.text.strip()

    def add_to_cart_and_verify(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='cPHDOP col-12-12']//button[text()='Add to cart']")))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        time.sleep(1)
        btn.click()
        changed_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button span")))
        return changed_btn.text