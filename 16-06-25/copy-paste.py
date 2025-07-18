# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# #open facebook
# # Keybord related action


# driver.get("https://www.facebook.com/")


# input1=driver.find_element(By.ID,"email")
# input2 = driver.find_element(By.ID,"pass")

# input1.send_keys("test@gmail.com")

# action = ActionChains(driver)

# # action.send_keys('a').perform()
# # action.send_keys('c').perform()


# action.send_keys(Keys.TAB)
# action.key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).perform()
# input1.send_keys(Keys.CONTROL, 'v')
# action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
# driver.find_element(By.XPATH,"//div[@class='_9lsb _9ls8']").click()


# time.sleep(5)
# driver.close()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open Facebook
driver.get("https://www.facebook.com/")
time.sleep(3)  # Let the page load

# Find the email and password input fields
email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "pass")

# Type the email
email_input.send_keys("test@gmail.com")

# Create ActionChains instance
action = ActionChains(driver)

# Select and copy the email using keyboard (Ctrl + A, Ctrl + C)
email_input.click()
action.key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).perform()

# Click on password field and paste (Ctrl + V)
password_input.click()
action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

driver.find_element(By.XPATH,"//div[@class='_9lsb _9ls8']").click()

# Optional wait to observe result before closing
time.sleep(5)

# Close browser
driver.quit()
