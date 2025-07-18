from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver =webdriver.Chrome()
driver.maximize_window()
#open facebook
# excepted_title = "Facebook – log in or sign up"
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
driver.implicitly_wait(10)

iframe = driver.find_element(By.XPATH,"//iframe[@class='demo-frame lazyloaded']") # need to find the xpath
driver.switch_to.frame(iframe)

src = driver.find_element(By.XPATH,"//img[@alt='The peaks of High Tatras']")
dest = driver.find_element(By.ID,"trash") #id="trash"

act  = ActionChains(driver)
act.drag_and_drop(src,dest).perform()

time.sleep(3)
driver.close()