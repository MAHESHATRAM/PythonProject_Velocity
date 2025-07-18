def test_google_search(driver):
    driver.get("https://www.saucedemo.com/")
    assert "Bing" in driver.title  # This will fail intentionally
