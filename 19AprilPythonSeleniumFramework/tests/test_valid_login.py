import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from Utils.logger import get_logger
from Utils.json_reader import load_json_data

logger = get_logger(__name__)
login_data = load_json_data("/Users/ranjeetkendre/Documents/AutomationProjects/19AprilPythonSeleniumFramework/data/product_data.json")

@pytest.mark.usefixtures("setup")
class TestValidLogin:

    def test_valid_login_from_json(self):
        login = LoginPage(self.driver)
        login.open_login_modal()

        username = login_data["login"]["username"]
        password = login_data["login"]["password"]

        login.login(username, password)
        logger.info(f"Attempted login with username: {username}")

        assert login.is_login_successful(), "Login failed with valid credentials"
        logger.info("Login successful")

        # Optional logout step
        home = HomePage(self.driver)
        home.logout()
        logger.info("User logged out after successful login.")
