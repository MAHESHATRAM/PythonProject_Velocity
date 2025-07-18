import time
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_flipkart_flow(driver, wait):
    driver.get("https://www.flipkart.com")

    home = HomePage(driver, wait)
    search = SearchResultsPage(driver, wait)
    product = ProductPage(driver, wait)
    cart = CartPage(driver, wait)

    home.close_login_popup()
    home.search_for_product("mobile")
    assert "results for" in search.verify_results_message()

    search.scroll_down()
    
    
    
    product_price = search.get_product_price(9)
    print("💰 Product List Price:", product_price)

    search.add_to_compare([9, 10])
    tray = search.verify_compare_tray()
    print("✅ Compare tray:", tray.text)
    # product_price = search.get_product_price_by_index(9)
    # print("✅ Product List Price:", product_price)

    product_name = search.get_product_name_and_click(9)
    print("🔍 Product Name :",product_name)
    time.sleep(5)

    product.switch_to_product_tab()
    title = product.get_product_title()
    print("🔍 Product Title:", title)
    assert product_name.lower() in title.lower()

    btn_text = product.add_to_cart_and_verify()
    print("✅ Button changed to:", btn_text)

    cart.wait_for_cart()
    cart_amount_text = cart.get_total_amount()
    print("🛒 Cart Total Amount:", cart_amount_text)
    
    
    
    fee_text = cart.get_platform_fee()
    platform_fee_clean = cart.clean_price(fee_text)

    # Default fee to 0 if None
    if platform_fee_clean is None:
        print("ℹ️ Platform fee not found — defaulting to 0.")
        platform_fee_clean = 0

    # Get product price and cart total
    product_price_clean = cart.clean_price(product_price)
    cart_total_clean = cart.clean_price(cart_amount_text)

    print(f"[DEBUG] product_price_clean     = {product_price_clean} ({type(product_price_clean)})")
    print(f"[DEBUG] cart_total_clean        = {cart_total_clean} ({type(cart_total_clean)})")

    expected_total = product_price_clean + platform_fee_clean
    print(f"[DEBUG] expected_total          = {expected_total}")

    expected_total == cart_total_clean, \
        f"❌ Price mismatch: expected = {expected_total}, actual cart = {product_price_clean}"

    print("✅ Cart amount matches product price + platform fee.")



    msg = cart.increase_quantity()
    assert "QUANTITY to '2'" in msg
    cart.remove_product()
    assert cart.verify_empty_cart()
    filename = f"empty_cart_{int(time.time())}.png"
    cart.driver.save_screenshot(filename)
    print("✅ Empty cart verified.")