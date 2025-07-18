import pytest
from pages.HomePage import HomePage
from pages.ContactPage import ContactPage
from Utils.logger import get_logger
import time

logger = get_logger(__name__)

@pytest.mark.usefixtures("setup")
class TestContactForm:

    def test_submit_contact_form(self):
        home = HomePage(self.driver)
        contact = ContactPage(self.driver)

        home.open_contact_popup()
        logger.info("Contact popup opened")

        contact.fill_contact_form("test@demo.com", "Ranjeet", "This is a test via ContactPage class.")
        logger.info("Contact form filled")

        contact.send_contact_form()
        logger.info("Sent contact form")

        try:
            alert = self.driver.switch_to.alert
            logger.info(f"Alert: {alert.text}")
            alert.accept()
        except:
            logger.warning("No alert appeared")

        time.sleep(2)
