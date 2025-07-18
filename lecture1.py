from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com")

# Fill the form
driver.find_element(By.XPATH, "//input[@placeholder='Full Name']").send_keys("MaheshAtram")
driver.find_element(By.ID, 'userEmail').send_keys("mahesh@gamil.com")
driver.find_element(By.XPATH, "//textarea[@placeholder='Current Address']").send_keys("Pune")
driver.find_element(By.ID, 'permanentAddress').send_keys("Nagpure")

# Submit the form
driver.find_element(By.ID, 'submit').click()

# Wait for output to appear
wait = WebDriverWait(driver, 10)
output = wait.until(EC.visibility_of_element_located((By.ID, 'output')))

# Fetch and print the submitted data
name_output = driver.find_element(By.ID, 'name').text
email_output = driver.find_element(By.ID, 'email').text
current_addr_output = driver.find_element(By.XPATH, "//p[@id='currentAddress']").text
permanent_addr_output = driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text

print("✅ Submitted Output:")
print(name_output)
print(email_output)
print(current_addr_output)
print(permanent_addr_output)

# Optional: Verification
assert "MaheshAtram" in name_output
assert "mahesh@gamil.com" in email_output
assert "Pune" in current_addr_output
assert "Nagpure" in permanent_addr_output

time.sleep(5)
driver.quit()
