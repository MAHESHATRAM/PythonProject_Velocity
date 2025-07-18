
# What is the Automation testing
# - At is the process if using specilized tool to execute test cases
# automatically , compaire actual outcome with exepected result and report defects 
# it reduce manual efforts and improve effeciency , accuracy and speed.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome Dev\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options=options, executable_path=r"C:\Program Files (x86)\Google\chromedriver.exe", )
driver.get("https://www.google.com/")