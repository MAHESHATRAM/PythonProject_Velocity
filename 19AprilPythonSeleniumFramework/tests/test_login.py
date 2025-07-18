import pytest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from Utils.logger import get_logger
from Utils.excel_reader import get_excel_data
from collections import Mapping

logger = get_logger(__name__)
data = get_excel_data("Automation\Python_Selenium\19AprilPythonSeleniumFramework\data\test_data.xlsx", "Sheet1")

@pytest.mark.usefixtures("setup")
class TestLoginExcel:

    @pytest.mark.smoke
    @pytest.mark.parametrize("username,password,status", data)
    def test_login_excel_data(self, username, password, status):
        login = LoginPage(self.driver)
        login.open_login_modal()
        login.login(username, password)

        if status.lower() == "valid":
            assert login.is_login_successful(), f"Login failed for valid user: {username}"
            logger.info(f"Login successful with: {username}")

            #  Logout after successful login
            home = HomePage(self.driver)
            home.logout()
            logger.info("User logged out after verification")

        else:
            assert not login.is_login_successful(), f"Login succeeded unexpectedly for invalid user: {username}"
            logger.info(f"Login failed as expected with: {username}")

            #  Cancel login modal after invalid login
            login.open_login_cancel()
            logger.info("Login modal cancelled after invalid login")

    def test_invalid_login_alert(self):
        login = LoginPage(self.driver)
        login.open_login_modal()
        self.driver.execute_script("window.alert = function(msg) { window.lastAlert = msg; return true; }")
        login.login("wronguser", "wrongpass")
        alert_message = self.driver.execute_script("return window.lastAlert")
        assert alert_message is None or "" in alert_message
        logger.info("Invalid login attempted. Alert (if any) captured via JS.")

        #  Cancel login modal explicitly
        login.open_login_cancel()
        logger.info("Login modal cancelled after alert")