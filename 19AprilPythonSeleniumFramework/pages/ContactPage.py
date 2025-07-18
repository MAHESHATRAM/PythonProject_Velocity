from selenium.webdriver.common.by import By
from pages.BasePage import basePage

class ContactPage(basePage):

    CONTACT_EMAIL_INPUT = (By.ID, "recipient-email")
    CONTACT_NAME_INPUT = (By.ID, "recipient-name")
    CONTACT_MESSAGE_INPUT = (By.ID, "message-text")
    SEND_MESSAGE_BTN = (By.XPATH, "//button[text()='Send message']")
    CLOSE_BTN = (By.XPATH, "//div[@id='exampleModal']//button[text()='Close']")

    def fill_contact_form(self, email, name, message):
        self.enter_text(self.CONTACT_EMAIL_INPUT, email)
        self.enter_text(self.CONTACT_NAME_INPUT, name)
        self.enter_text(self.CONTACT_MESSAGE_INPUT, message)

    def send_contact_form(self):
        self.click(self.SEND_MESSAGE_BTN)

    def close_contact_popup(self):
        self.click(self.CLOSE_BTN)
