import pytest
from selenium import webdriver
from datetime import datetime
import os

# Create screenshots folder if it doesn't exist
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    # Attach the driver to the node for access in hooks
    request.node.driver = driver
    yield driver
    driver.quit()

# Hook to capture screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to get the report object
    outcome = yield
    report = outcome.get_result()

    # Only act on actual test call phase failures
    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(SCREENSHOT_DIR, file_name)
            driver.save_screenshot(file_path)
            print(f"\nScreenshot saved: {file_path}")
