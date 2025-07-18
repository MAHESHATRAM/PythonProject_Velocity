import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.CartPage import CartPage
from Utils.logger import get_logger
from Utils.json_reader import load_json_data
import time

logger = get_logger(__name__)
product_data = load_json_data("Automation\Python_Selenium\19AprilPythonSeleniumFramework\data\product_data.json")

@pytest.mark.usefixtures("setup")
class TestCartFlow:

    @pytest.mark.parametrize("product", product_data["products"])
    def test_valid_login_add_and_remove_cart(self, product):
        login = LoginPage(self.driver)
        login.open_login_modal()
        login.login("pavanol", "test@123")
        logger.info("User logged in successfully")

        home = HomePage(self.driver)
        home.add_product_to_cart(product)
        logger.info(f"Product '{product}' added to cart")

        home.goto_cart()

        cart = CartPage(self.driver)

        # Debug: Print products present in cart
        logger.info("Checking if product is present in cart...")
        try:
            wait = WebDriverWait(self.driver, 10)
            products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//td[2]")))
            for item in products:
                logger.info(f"Found product in cart: {item.text}")
        except Exception as e:
            logger.error("Could not load cart products")

        # Verify product presence
        assert cart.check_product_in_cart(product), f"'{product}' not found in cart!"
        logger.info("Product found in cart and verified")

        time.sleep(3)
        cart.delete_product_from_cart(product)
        logger.info("Product deleted from cart")

        home.goto_Home()

