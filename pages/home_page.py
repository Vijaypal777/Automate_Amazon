from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product_name):
        search_input = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_input.clear()
        search_input.send_keys(product_name)
        self.driver.find_element(By.ID, "nav-search-submit-button").click()
