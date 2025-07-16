from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class FlipkartCartAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)

    def open_flipkart(self):
        self.driver.get("https://www.flipkart.com")
        self.driver.maximize_window()

    def close_login_popup(self):
        try:
            close_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'\u2715')]")))
            close_btn.click()
        except:
            print("No login pop-up found.")

    def search_mobile(self):
        search_box = self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.send_keys("mobile")
        search_box.send_keys(Keys.RETURN)

    def verify_result_message(self):
        result_msg = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='BUOuZu']")))
        assert "results for" in result_msg.text
        print("✅ Search result message verified:", result_msg.text)

    def scroll_products(self):
        for _ in range(3):
            self.driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(2)

    def select_compare_checkbox(self):
        compare_spans = self.driver.find_elements(By.XPATH, "//span[text()='Add to Compare']")
        if len(compare_spans) < 11:
            raise Exception("Not enough products to compare.")
        for i in [9, 10]:
            checkbox = compare_spans[i].find_element(By.XPATH, "./preceding::input[@type='checkbox'][1]")
            self.driver.execute_script("arguments[0].click();", checkbox)
        print("✅ Compare checkboxes selected.")

    def verify_compare_tray(self):
        compare_tray = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'COMPARE')]")))
        print("✅ Compare tray visible:", compare_tray.text)

    def click_10th_product(self):
        compare_spans = self.driver.find_elements(By.XPATH, "//span[text()='Add to Compare']")
        checkbox_10 = compare_spans[9].find_element(By.XPATH, "./preceding::input[@type='checkbox'][1]")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox_10)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", checkbox_10)

        product_block = compare_spans[9].find_element(By.XPATH, "./ancestor::div[@class='tUxRFH']")
        product_name_element = product_block.find_element(By.XPATH, ".//div[@class='KzDlHZ']")
        product_name = product_name_element.text
        print("📦 10th Product Name:", product_name)

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_name_element)
        time.sleep(1)
        product_name_element.click()
        return product_name

    def switch_to_product_tab(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        print("✅ Switched to product detail tab.")

    def add_to_cart_and_verify(self, expected_product_name):
        product_title_element = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[@class='VU-ZEz'] | //span[@class='B_NuCI']")))
        product_title = product_title_element.text.strip()

        if expected_product_name.lower() in product_title.lower():
            print("✅ Correct product detail page opened.")
        else:
            print("⚠️ Product name mismatch! Still continuing...")

        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='cPHDOP col-12-12']//button[text()='Add to cart']")))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_button)
        time.sleep(1)
        add_to_cart_button.click()
        print("✅ Clicked 'Add to cart' for:", product_title)

        going_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button span")))
        print("✅ Button changed to:", going_btn.text)

    def verify_total_amount(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Price details']")))
        cart_amount = self.driver.find_element(By.XPATH,
            "//div[text()='Total Amount']/following-sibling::div//div[contains(@class, '_1dqRvU')]").text.strip()
        print("🛒 Cart Total Amount:", cart_amount)

    def increase_quantity_and_verify(self):
        plus_btn = self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[@class='atHedL']//following-sibling::button[text()='+']")))
        time.sleep(2)
        plus_btn.click()
        print("✅ Clicked '+' button to increase quantity.")
        popup_msg = self.wait.until(EC.presence_of_element_located((
            By.XPATH, "//div[contains(text(),'QUANTITY to')]")))
        assert "QUANTITY to '2'" in popup_msg.text
        print("✅ Quantity updated popup:", popup_msg.text)

    def remove_product_and_verify(self):
        try:
            remove_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Remove']")))
            remove_btn.click()
            print("🗑️ Clicked on cart item's 'Remove' option.")
        except TimeoutException:
            print("❌ Could not find or click the initial 'Remove' button.")

        dialog = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='container']//child::div//child::div//child::div//child::button[text()='\u2715']")))
        assert self.driver.find_element(By.XPATH, "//div[text()='Cancel']")
        confirm_remove = self.driver.find_element(By.XPATH, "//div[text()='Remove']")
        print("✅ Remove confirmation popup appeared.")
        confirm_remove.click()

        empty_cart_msg_1 = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[text()='Missing Cart items?']")))
        empty_cart_msg_2 = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[text()='Login to see the items you added previously']")))

        if empty_cart_msg_1.is_displayed() and empty_cart_msg_2.is_displayed():
            print("✅ Empty cart screen message verified:")
            print("-", empty_cart_msg_1.text)
            print("-", empty_cart_msg_2.text)
        else:
            print("❌ One or both empty cart messages not visible.")

    def run(self):
        try:
            self.open_flipkart()
            self.close_login_popup()
            self.search_mobile()
            self.verify_result_message()
            self.scroll_products()
            self.select_compare_checkbox()
            self.verify_compare_tray()
            product_name = self.click_10th_product()
            time.sleep(5)
            self.switch_to_product_tab()
            self.add_to_cart_and_verify(product_name)
            time.sleep(5)
            self.verify_total_amount()
            self.increase_quantity_and_verify()
            self.remove_product_and_verify()
        finally:
            self.driver.quit()

if __name__ == "__main__":
    FlipkartCartAutomation().run()
