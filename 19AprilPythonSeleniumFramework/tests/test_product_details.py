import pytest
from pages.HomePage import HomePage
from Utils.logger import get_logger
from generic_utils.actions_util import ActionUtility
from generic_utils.javascript_util import JavaScriptUtility
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger(__name__)

@pytest.mark.usefixtures("setup")
class TestProductDetails:

    def test_verify_product_details_page(self):
        product_name = "Nokia lumia 1520"

        home = HomePage(self.driver)
        action_util = ActionUtility(self.driver)
        js_util = JavaScriptUtility(self.driver)

        # Get product element by name (link text)
        product_element = home.get_product_element_by_name(product_name)

        # Hover over the product
        action_util.hover_over_element(product_element)
        logger.info(f"Hovered over product: {product_name}")

        # Click using JavaScript
        js_util.click_element_js(product_element)
        logger.info(f"Clicked product using JS: {product_name}")

        # Wait for product details page to load and assert product name
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//h2[contains(text(),'{product_name}')]"))
            )
            logger.info(f"Product details page loaded successfully for: {product_name}")
        except Exception:
            logger.error(f"{product_name} not found on product details page")
            assert False, f"{product_name} not found on product details page"