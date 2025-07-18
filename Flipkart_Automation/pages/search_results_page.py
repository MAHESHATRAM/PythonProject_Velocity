from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .base_page import BasePage

class SearchResultsPage(BasePage):
    def verify_results_message(self):
        result_msg = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='BUOuZu']")))
        assert "results for" in result_msg.text
        return result_msg.text

    def scroll_down(self, times=3):
        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(2)

    def add_to_compare(self, indices):
        spans = self.driver.find_elements(By.XPATH, "//span[text()='Add to Compare']")
        if len(spans) < max(indices) + 1:
            raise Exception("Not enough products.")
        for i in indices:
            checkbox = spans[i].find_element(By.XPATH, "./preceding::input[@type='checkbox'][1]")
            self.driver.execute_script("arguments[0].click();", checkbox)

    def verify_compare_tray(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'COMPARE')]")))

    def get_product_name_and_click(self, index):
        spans = self.driver.find_elements(By.XPATH, "//span[text()='Add to Compare']")
        block = spans[index].find_element(By.XPATH, "./ancestor::div[@class='tUxRFH']")
        name_elem = block.find_element(By.XPATH, ".//div[@class='KzDlHZ']")
        name = name_elem.text
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", name_elem)
        time.sleep(1)
        name_elem.click()
        return name
    
    
    def get_product_price(self, index):
        """
        Gets the price of the mobile at given index from Flipkart search results.
        :param driver: Selenium WebDriver object
        :param index: Index (0-based) of the mobile in the search results
        :return: Price of the mobile as string
        """
        # Wait to ensure page is fully loaded
        time.sleep(2)

        # Scroll down to ensure all items are loaded
        self.driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(1)

        # Get all product price elements associated with 'Add to Compare'
        add_to_compare_spans = self.driver.find_elements(By.XPATH, "//span[text()='Add to Compare']")
        try:
            if index >= len(add_to_compare_spans):
                raise IndexError(f"❌ Only {len(add_to_compare_spans)} products found, but index {index} was requested.")

            # Get the parent block of the indexed item
            product_block = add_to_compare_spans[index].find_element(By.XPATH, "./ancestor::div[@class='tUxRFH']")
            print("product_block: ",product_block)
            # Find the price inside the product block
            price_elem = product_block.find_element(By.XPATH, ".//div[contains(@class,'Nx9bqj')]")
            price_text = price_elem.text.replace("₹", "").replace(",", "").strip()

            print(f"✅ Mobile at index {index} has price: ₹{price_text}")
            return price_text
        except NoSuchElementException:
            print(f"❌ Price not found for product at index {index}")
            return None