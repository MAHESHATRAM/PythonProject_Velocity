

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC


class basePage:

    def __init__(self,driver, timeout =10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()

    def enter_text(self, by_locator,text):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.clear()
        element.send_keys(text)
    
    def get_text(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        return element.text
    
    def is_visible(self, by_locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(by_locator)).is_displayed()
        except:
            return False
    
    def wait_for_alert_and_accept(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    





