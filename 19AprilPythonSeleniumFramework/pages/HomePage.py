from selenium.webdriver.common.by import By
from .BasePage import basePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time

class HomePage(basePage):

    # ---------- Locators ----------
    LOGOUT_LINK = (By.XPATH, "//a[text()='Log out']")
    CART_LINK = (By.ID, "cartur")
    HOME_LINK = (By.XPATH, "//a[text()='Home ']")
    CONTACT_LINK = (By.LINK_TEXT, "Contact")
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[text()='Add to cart']")
    CONTACT_MODAL = (By.ID, "exampleModal")

    def add_product_to_cart(self, product_name):
        """
        Adds a specified product to the cart by product link text.
        Includes retry logic to handle stale elements.
        """
        retry_count = 2
        for attempt in range(retry_count):
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, product_name))
                ).click()

                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
                ).click()

                self.wait_for_alert_and_accept()
                self.driver.back()

                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(self.CART_LINK)
                )
                break

            except StaleElementReferenceException as e:
                print(f"[Retry {attempt+1}] Caught StaleElementReferenceException: {e}")
                time.sleep(2)
                continue

            except TimeoutException as e:
                print(f"[Timeout] Element not clickable: {e}")
                raise

    def goto_cart(self):
        """Navigates to the cart page."""
        self.click(self.CART_LINK)

    def goto_Home(self):
        """Navigates to the home page."""
        self.click(self.HOME_LINK)

    def logout(self):
        """Logs out the current user."""
        self.click(self.LOGOUT_LINK)

    def get_product_element_by_name(self, product_name, timeout=10):
        """
        Waits for and returns the product WebElement using the product name (link text).
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, product_name)))
            return element
        except TimeoutException:       
            return None

    def open_contact_popup(self):
        """
        Opens the contact popup and waits for it to be visible.
        """
        self.click(self.CONTACT_LINK)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.CONTACT_MODAL)
        )
