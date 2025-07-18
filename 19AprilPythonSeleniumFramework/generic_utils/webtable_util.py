from selenium.webdriver.common.by import By

class WebTableUtility:
    def __init__(self, driver):
        self.driver = driver

    def get_table_data(self, table_locator):
        table = self.driver.find_element(*table_locator)
        rows = table.find_elements(By.TAG_NAME, "tr")
        data = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            data.append([col.text.strip() for col in cols])
        return data

    def get_cell_value(self, table_locator, row_num, col_num):
        table = self.driver.find_element(*table_locator)
        rows = table.find_elements(By.TAG_NAME, "tr")
        if row_num >= len(rows):
            return None
        cols = rows[row_num].find_elements(By.TAG_NAME, "td")
        if col_num >= len(cols):
            return None
        return cols[col_num].text.strip()

