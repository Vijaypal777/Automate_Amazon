from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def select_products(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "a-autoid-1-announce"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "a-autoid-2-announce"))
        ).click()
