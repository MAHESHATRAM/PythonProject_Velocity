import pytest
from selenium import webdriver
import os
from datetime import datetime

def pytest_addoption(parser):
    parser.addoption(
        "--my-browser", action="store", default="chrome", help="Browser to use: chrome or firefox"
    )
    parser.addoption(
        "--login-source", action="store", default="excel", help="Data source: excel or json"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--my-browser") or "chrome"

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"Browser '{browser}' is not supported.")

    driver.maximize_window()
    driver.get("https://www.demoblaze.com/")
    request.cls.driver = driver

    yield

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    # This hook captures screenshots when a test fails
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = getattr(item.cls, "driver", None)
        if driver:
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshot_dir, file_name)

            driver.save_screenshot(screenshot_path)
