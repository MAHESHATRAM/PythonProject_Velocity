import pytest
import requests
from selenium.webdriver.common.by import By
from Utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.usefixtures("setup")
class TestBrokenLinks:

    def test_all_links_on_page(self):
        all_links = self.driver.find_elements(By.TAG_NAME, "a")
        logger.info(f"🔗 Total links found: {len(all_links)}")

        for link in all_links:
            url = link.get_attribute("href")

            # Skip if href is empty or None
            if not url:
                logger.warning(" Skipping empty href link.")
                continue

            try:
                response = requests.head(url, timeout=5)
                status = response.status_code

                if status >= 400:
                    logger.error(f" Broken Link: {url} returned status code {status}")
                else:
                    logger.info(f" Valid Link: {url} returned status code {status}")
            except requests.exceptions.RequestException as e:
                logger.error(f" Exception for URL: {url} | Error: {str(e)}")
