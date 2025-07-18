from selenium.webdriver.common.action_chains import ActionChains

class ActionUtility:
    def __init__(self, driver):
        self.driver = driver

    def hover(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, element):
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, element):
        ActionChains(self.driver).context_click(element).perform()

    def drag_and_drop(self, source, target):
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def hover_over_element(self, element):
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            print("Hovered over element successfully")
        except Exception as e:
            print(f"Error while hovering over element: {e}")