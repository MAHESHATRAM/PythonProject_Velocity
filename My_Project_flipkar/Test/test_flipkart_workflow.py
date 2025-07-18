import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from conftest import driver
import time
wait = WebDriverWait(driver, 20)

def test_flipkart_end_to_end(driver):
    home = HomePage(driver)
    search = SearchResultsPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    driver.get("https://www.flipkart.com")
    try:
        close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]")))
        close_btn.click()
    except:
        print("No login pop-up found.")
    home.search_product("mobile")
    home.wait_for_processing_to_finish()
    
    # Verify search result text
    result_text = search.get_results_text()
    assert "results for" in result_text
    assert "mobile" in result_text.lower()


    # Compare 10th and 11th items
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)
    search.select_compare_item(10)
    search.select_compare_item(11)
    compare_texts = search.compare_tray_items_text()
    print("compare_texts : ",compare_texts)
    # assert len(compare_texts) == 2, f"❌ Expected 2 items in compare tray, found {len(compare_texts)}"
    assert all("COMPARE" in text.upper() for text in compare_texts), f"❌ Compare tray texts mismatch: {compare_texts}"
    print("✅ Compare tray texts:", compare_texts)
    # Click 10th phone
    search.click_product_by_index(10)

    # Switch to new tab
    driver.switch_to.window(driver.window_handles[1])


    # On product page
    price = product.get_product_price()
    product_name = product.get_product_name()
    product.add_to_cart()
    assert product.verify_add_to_cart_text() == "GOING TO CART"

    # Cart verification
    cart.verify_total_amount(price)
    cart.increase_quantity()
    assert cart.get_qty_popup_text().startswith(f"You've changed '{product_name}' QUANTITY to '2'")

    # Remove product
    cart.remove_item()
    cart.confirm_remove()
    assert cart.get_remove_confirmation_text().startswith(f'"{product_name}" from your cart')
    assert cart.is_cart_empty_message_displayed()
