from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(by_locator)
        )
        element.click()
    def enter_text(self, by_locator, text):

        self.driver.find_element(*by_locator).send_keys(text)

    def get_text(self, by_locator):
        return self.driver.find_element(*by_locator).text

    def wait_for_element(self, by_locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))

    def wait_for_processing_to_finish(self, timeout=10):
        # Common Flipkart loader: spinner, overlay, etc. (check your actual loader class)
        loader_locator = (By.CSS_SELECTOR, "._2YsvKq")  # Flipkart uses a class like this sometimes

        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(loader_locator))
            WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located(loader_locator))
        except:
            pass  # If no loader appears, just continue silently
