from selenium.webdriver.common.by import By
from selenium import webdriver

from pip._vendor import requests
driver = webdriver.Chrome()
driver.maximize_window()


driver.get("http://testphp.vulnweb.com/")
all_links = driver.find_elements(By.TAG_NAME,'a')

print(f"Toatal links :{len(all_links)}")
broken_links = 0
for elem in all_links:
    url = elem.get_attribute("href")
    
    if url is None or url.strip() == "":
        
        print("Url is empty")
        continue
    try:
        response = requests.head(url,allow_redirects=True,timeout=5)
        if response.status_code >= 400:
            print(f"Broken Link{response.status_code}-->{url} is broken Link")
        else:
            print(f"{response.status_code}-->{url} is a valid link")
    except requests.exceptions.RequestException as e:
        print(f"Error checking Url:{url}:{e}")
        broken_links=+1
print({broken_links})