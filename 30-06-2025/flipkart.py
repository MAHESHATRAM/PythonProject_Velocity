from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    # Step: Click on the phone name from the same block
    # Step: Click on the phone name from the same block
    
    
        # 1️⃣ Get the product block from compare span
    # Step: Get the product block from the compare span
    product_block = compare_spans[9].find_element(By.XPATH, "//div[@class='Y7XAvH']")  # Adjusted to relative XPath
    print("Product_block: ",product_block.text)
    # Define title extractor
    # def get_phone_title(product_block):
    #     for xpath in [
    #         "//div[@id='container']|//div[@class='_75nlfW']"             # Alternate layout
    #     ]:
    #         try:
    #             return product_block.find_element(By.XPATH, xpath)
    #         except:
    #             continue
    #     raise Exception("Phone title not found in product block")

    # Extract and print phone name
    # phone_title_element = get_phone_title(product_block)
    phone_title_element = driver.find_element(By.XPATH, "//div[@id='container']|//div[@class='_75nlfW']").click()
    # phone_name = phone_title_element.text.strip()
    # print("📱 10th Phone Name:", phone_name)
    print("line no 88")
    # time.sleep(5)

    # Click the phone link
    # phone_link = phone_title_element.find_element(By.XPATH, "//div[@id='container']|//div[@class='_75nlfW']")
    # driver.execute_script("arguments[0].click();", phone_link)
    # print("🖱️ Clicked on phone link:", phone_name)

    # Switch to product tab
    # driver.switch_to.window(driver.window_handles[1])

    # Click "Add to cart"
    # try:
    #     add_to_cart_btn = wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, "//button[text()='Add to cart']")))
    #     add_to_cart_btn.click()
    # except Exception as e:
    #     print("Add to cart button not found:", e)

    # # Verify button changed
    # updated_btn = driver.find_element(By.XPATH, "//button[text()='Add to cart']")
    # assert "GO TO CART" in updated_btn.text.upper()
    # print("✅ Button changed after adding to cart:", updated_btn.text)

    # # Proceed to cart
    # updated_btn.click()





    # Assume a link opened a new tab
    # original_tab = driver.current_window_handle
    # wait = WebDriverWait(driver, 10)
    # wait.until(lambda d: len(driver.window_handles) > 1)

    # # Now switch to new tab
    # driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)

    # Step 10: Click on 'Add to cart'
    add_to_cart_button = driver.find_element(By.XPATH, "//button[@class='QqFHMw cNEU5Q J9Kkbj _7Pd1Fp']//child::span").click()
    # add_to_cart_button = wait.until(
    #     EC.presence_of_element_located((By.XPATH, "//button[@class='QqFHMw cNEU5Q J9Kkbj _7Pd1Fp']//child::span"))
    # )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_button)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", add_to_cart_button)
    print("✅ Clicked 'Add to cart'")
    

    # Step 11: Verify button changed
    new_btn_text = driver.find_element(By.XPATH, "//button").text
    assert "GO TO CART" in new_btn_text.upper()
    print("✅ Add to cart → Button changed:", new_btn_text)

    # Step 12: Go to cart page
    driver.find_element(By.XPATH, "//button[contains(., 'GO TO CART')]").click()

    # Step 13: Verify item in cart and total amount present
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Price details']")))
    cart_amount = driver.find_element(By.XPATH, "//div[text()='Total Amount']/following-sibling::span").text
    print("✅ Item added to cart. Total Amount:", cart_amount)

    # Step 14: Increase quantity
    plus_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='+']")))
    plus_btn.click()

    # Step 15: Verify popup message
    popup_msg = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'QUANTITY to')]")))
    assert "QUANTITY to '2'" in popup_msg.text
    print("✅ Quantity updated popup:", popup_msg.text)

    # Step 16: Click Remove
    remove_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Remove']")))
    remove_btn.click()

    # Step 17: Verify popup with Cancel and Remove
    dialog = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='dialog']")))
    assert driver.find_element(By.XPATH, "//div[text()='Cancel']")
    confirm_remove = driver.find_element(By.XPATH, "//div[text()='Remove']")
    print("✅ Remove confirmation popup appeared.")
    confirm_remove.click()

    # Step 18: Verify product removed
    time.sleep(3)
    removed_msg = wait.until(EC.presence_of_element_located(
        (By.XPATH, f"//div[contains(text(),'{phone_name}') and contains(text(),'from your cart')]")))
    print("✅ Product removed:", removed_msg.text)

    # Step 19: Verify empty cart screen message
    empty_cart_msg = driver.find_element(By.XPATH, "//div[contains(text(),'Missing Cart items?')]").text
    assert "Missing Cart items?" in empty_cart_msg
    print("✅ Empty cart message:", empty_cart_msg)

finally:
    driver.quit()
