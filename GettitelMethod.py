from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
import time

#open facebook
excepted_title = "Facebook – log in or sign up"
driver.get("https://www.facebook.com/")
time.sleep(5)
actual_title = driver.title

if excepted_title == actual_title:
    print("Correct tile")
else:
    print("Incorrect Title")
driver.close()


#XPATH //input[@class="inputtext _55r1 _6luy"]