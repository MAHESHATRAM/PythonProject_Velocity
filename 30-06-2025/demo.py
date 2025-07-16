from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

try:
    # Step 1: Open Flipkart
    driver.get("https://www.flipkart.com")
    driver.maximize_window()

    # Step 2: Close login pop-up
    
    try:
        close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]")))
        close_btn.click()
    except:
        print("No login pop-up found.")

    # Step 3: Search for 'mobile'
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.send_keys("mobile")
    search_box.send_keys(Keys.RETURN)
    # Step 4: Verify result message
    result_msg = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[@class='BUOuZu']")))
    assert "results for" in result_msg.text
    print("✅ Search result message verified:", result_msg.text)

    # Step 5: Scroll to load enough products
    for _ in range(3):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

    # Step 6: Click on compare checkboxes for 10th and 11th phones
    compare_spans = driver.find_elements(By.XPATH, "//span[text()='Add to Compare']")
    if len(compare_spans) < 11:
        raise Exception("Not enough products to compare.")
    for i in [9, 10]:
        checkbox = compare_spans[i].find_element(By.XPATH, "./preceding::input[@type='checkbox'][1]")
        
        driver.execute_script("arguments[0].click();", checkbox)
    print("✅ Compare checkboxes selected.")

    # Step 7: Verify compare tray
    compare_tray = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'COMPARE')]")))
    print("✅ Compare tray visible:", compare_tray.text)

    # Step 8: Click on 10th phone name
    # Step: Select 10th checkbox (index 9)
    compare_spans = driver.find_elements(By.XPATH, "//span[text()='Add to Compare']")
    if len(compare_spans) < 10:
        raise Exception("❌ Less than 10 compare spans found.")
    print("10 :",compare_spans[9])
    checkbox_10 = compare_spans[9].find_element(By.XPATH, "./preceding::input[@type='checkbox'][1]")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox_10)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", checkbox_10)
    print("✅ Clicked on 10th product checkbox.")


    # Step: Get the product block from the compare span
    product_block = compare_spans[9].find_element(By.XPATH, "//div[@class='Y7XAvH']")  # Adjusted to relative XPath
    print("Product_block: ",product_block.text)
    
   # Step: Get the 10th 'Add to Compare' element again
    compare_spans = driver.find_elements(By.XPATH, "//span[text()='Add to Compare']")

    # Ensure 10th product exists
    if len(compare_spans) < 10:
        raise Exception("❌ Less than 10 products found.")

    # Step: From the 10th 'Add to Compare', get the product block
    product_block = compare_spans[9].find_element(By.XPATH, "./ancestor::div[@class='tUxRFH']")

    # Step: Get the product name inside that block
    product_name_element = product_block.find_element(By.XPATH, ".//div[@class='KzDlHZ']")
    product_name = product_name_element.text
    print("📦 10th Product Name:", product_name)

    # Click to go to the product detail page
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_name_element)
    time.sleep(1)
    product_name_element.click()

    time.sleep(5)

        # Step 10: Click on 'Add to cart' button and verify state change
        # Click on 10th product

    
    # Step: Switch to new tab
    windows = driver.window_handles
    driver.switch_to.window(windows[1])  # assuming the new tab is at index 1
    print("✅ Switched to product detail tab.")

    # Step: Wait for product detail title to load
    product_title_element = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span[@class='VU-ZEz'] | //span[@class='B_NuCI']")))
    product_title = product_title_element.text.strip()
    print("🔍 Product detail page title:", product_title)

    # ✅ Optional: Check that the correct product is opened
    if product_name.lower() in product_title.lower():
        print("✅ Correct product detail page opened.")
    else:
        print("⚠️ Product name mismatch! Still continuing...")

    # Step: Wait for 'Add to cart' button and click
    add_to_cart_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='cPHDOP col-12-12']//button[text()='Add to cart']"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_button)
    time.sleep(1)

    # Capture text before click (optional check)
    before_click_text = add_to_cart_button.text.strip()
    print("🟡 Before Click Button Text:", before_click_text)

    # Click the button
    add_to_cart_button.click()
    print("✅ Clicked 'Add to cart' for:", product_title)

    # Step: Verify the button text changes to "GOING TO CART"
    # Verify button text changes to "GOING TO CART"
    going_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button span")))
    print("✅ Button changed to:", going_btn.text)



    time.sleep(5)
    # Step 12: Go to cart page
    # driver.find_element(By.XPATH, "//button[contains(., 'GO TO CART')]").click()

    # Wait for cart section with Price details (CSS version)
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Price details']")))

    # Step 10: Get Total Amount from cart
    cart_amount = driver.find_element(By.XPATH,"//div[text()='Total Amount']/following-sibling::div//div[contains(@class, '_1dqRvU')]").text.strip()

    print("🛒 Cart Total Amount:", cart_amount)

    # print(f"{label}: {value}")

    time.sleep(5)
    # Step 14: Increase quantity
    plus_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='atHedL']//following-sibling::button[text()='+']")))
    time.sleep(5)
    # Now click it safely
    plus_btn.click()
    print("✅ Clicked '+' button to increase quantity.")
    
    time.sleep(5)
    # Step 15: Verify popup message
    popup_msg = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'QUANTITY to')]")))
    assert "QUANTITY to '2'" in popup_msg.text
    print("✅ Quantity updated popup:", popup_msg.text)
    time.sleep(5)
    try:
        remove_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[text()='Remove']"
        )))
        remove_btn.click()
        print("🗑️ Clicked on cart item's 'Remove' option.")
    except TimeoutException:
        print("❌ Could not find or click the initial 'Remove' button.")
    
   


    # Step 17: Verify popup with Cancel and Remove
    dialog = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='container']//child::div//child::div//child::div//child::button[text()='✕']")))
    assert driver.find_element(By.XPATH, "//div[text()='Cancel']")
    confirm_remove = driver.find_element(By.XPATH, "//div[text()='Remove']")
    print("✅ Remove confirmation popup appeared.")
    confirm_remove.click()

    # Step 18: Verify product removed
    time.sleep(3)
    # Wait for the empty cart message block
    empty_cart_msg_1 = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='Missing Cart items?']"))
    )

    empty_cart_msg_2 = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[text()='Login to see the items you added previously']")))

    # Verify both messages
    if empty_cart_msg_1.is_displayed() and empty_cart_msg_2.is_displayed():
        print("✅ Empty cart screen message verified:")
        print("-", empty_cart_msg_1.text)
        print("-", empty_cart_msg_2.text)
    else:
        print("❌ One or both empty cart messages not visible.")

finally:
    driver.quit()
