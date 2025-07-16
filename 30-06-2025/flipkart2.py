import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_to_cart_and_verify_amount(driver):
    wait = WebDriverWait(driver, 15)

    # Step 1: Go to product list page (e.g. mobiles)
    driver.get("https://www.flipkart.com/search?q=mobile")

    # Step 2: Close login pop-up if present
    try:
        close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]")))
        close_button.click()
    except:
        pass  # If not found, skip

    # Step 3: Capture the price of the first product
    product = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class,'_1AtVbE')])[2]")))
    product_price_elem = product.find_element(By.XPATH, ".//div[contains(@class, '_30jeq3')]")
    product_price_text = product_price_elem.text  # Example: ₹14,999
    product_price = int(''.join(filter(str.isdigit, product_price_text)))

    # Step 4: Click to open product details in new tab
    product.find_element(By.XPATH, ".//a").click()
    driver.switch_to.window(driver.window_handles[1])  # Switch to new tab

    # Step 5: Click on "Add to cart"
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]")))
    add_to_cart_button.click()

    # Step 6: Wait for button to change to "Going to cart"
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//button"), "Going to cart"))

    # Step 7: Verify cart page loaded and item present
    cart_item = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Cart')] | //div[contains(text(),'My Cart')]")))
    assert cart_item is not None, "Cart page did not load correctly"

    # Step 8: Verify total amount in cart
    total_amount_elem = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Total Amount')]/following-sibling::span")))
    cart_total_text = total_amount_elem.text
    cart_total = int(''.join(filter(str.isdigit, cart_total_text)))

    assert product_price == cart_total, f"Price mismatch! List: ₹{product_price}, Cart: ₹{cart_total}"
