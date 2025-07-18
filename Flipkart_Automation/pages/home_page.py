from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class HomePage(BasePage):
    def close_login_popup(self):
        """
        Closes the Flipkart login popup if it appears.
        """
        try:
            close_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]"))
            )
            close_btn.click()
            print("✅ Login popup closed.")
        except TimeoutException:
            print("ℹ️ No login popup found — continuing.")
        except Exception as e:
            print(f"❌ Failed to close login popup: {e}")


    def search_for_product(self, query):
        search_box = self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)