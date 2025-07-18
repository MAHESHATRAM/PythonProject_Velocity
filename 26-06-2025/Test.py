import pytest
from selenium import webdriver

# ------------------------
# Fixtures: Replacing TestNG's setup/teardown annotations
# ------------------------

@pytest.fixture(scope="session", autouse=True)
def setup_system_config():
    print("\n@BeforeSuite setup system confign")
    yield
    print("@AfterSuite setup system confign")

@pytest.fixture(scope="module", autouse=True)
def login_application():
    print("@BeforeTest -- Login Application")
    yield
    print("@AfterTest -- FacebookLogout")

@pytest.fixture(scope="class", autouse=True)
def enter_url():
    print("@BeforeClass -- Enter URL")
    yield
    print("AfterClass -- Close browser")

@pytest.fixture(scope="function", autouse=True)
def launch_browser():
    print("@BeforeMethod -- Launch Browser")
    # You can uncomment below to actually launch browser:
    # driver = webdriver.Chrome()
    # yield driver
    yield
    print("@AfterMethod -- DeleteCookies")

# ------------------------
# Test Cases
# ------------------------

class TestFacebook:

    def test_facebook_logo_1(self):
        print("Facebook 1 logo verify")

    def test_facebook_logo_2(self):
        print("Facebook 2 logo verify")

    def test_demo(self):
        try:
            i = 10 / 0
            print(i)
        except ZeroDivisionError as e:
            print(f"Caught error: {e}")
        print("Demo")
