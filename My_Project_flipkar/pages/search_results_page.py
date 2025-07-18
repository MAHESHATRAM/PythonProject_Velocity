from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver
from selenium import webdriver



class SearchResultsPage(BasePage):
    RESULT_SUMMARY_TEXT = (By.XPATH, "//span[@class='BUOuZu']")

    def get_results_text(self):
        return self.get_text(self.RESULT_SUMMARY_TEXT)

    
    def select_compare_item(self, index):
        checkbox_xpath = f"(//label[.//span[contains(text(),'Compare')]])[{index}]"
        checkbox = self.driver.find_element(By.XPATH, checkbox_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", checkbox)

    def compare_tray_items_text(self):
        tray_locator = (By.XPATH, "//*[contains(text(),'COMPARE')]")
        
        ## Scroll down slightly to trigger lazy loading
        self.driver.execute_script("window.scrollBy(0, 400);")
        time.sleep(2)  
        
        tray_items = self.driver.find_elements(*tray_locator)
        return [el.text for el in tray_items]



    # driver = webdriver.Chrome()
def click_product_by_index(self, index):
    # Get all product links by going from title div → parent <a>
    product_elements = self.driver.find_elements(By.XPATH, "//div[@class='_4rR01T']/parent::a")

    if len(product_elements) < index:
        raise IndexError(f"❌ Only {len(product_elements)} products found. Can't click index {index}.")

    element = product_elements[index - 1]

    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(1)
    self.driver.execute_script("arguments[0].click();", element)

    print(f"✅ Clicked on product #{index}: {element.text.strip()}")






