import pytest
from selenium import webdriver

@pytest.fixture()
def setup_system_config():
    print("setup sysyem config")

@pytest.fixture()
def login_application():
    print("login application")

@pytest.fixture()
def enter_url():
    print("Enter URL")

@pytest.fixture()
def launch_brower():
    print("Launch brower config")

class TestDemo:
    def test_faceBook_logo_1(self):
        print("Facebook 1 logo verify")
    
    def test_faceBook_logo_2(self):
        print("Facebook 2 logo verify")
    
    def test_logo(self):
        try:
            i = 10/0
            print(i)
        except ZeroDivisionError as e:
            print(f"Caught error: {e}")
