class JavaScriptUtility:
    def __init__(self, driver):
        self.driver = driver

    def click_with_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def highlight_element(self, element):
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
    
    def click_element_js(self, element):
        try:
            self.driver.execute_script("arguments[0].click();", element)
            print("Clicked element using JavaScript successfully")
        except Exception as e:
            print(f"Error clicking element with JavaScript: {e}")