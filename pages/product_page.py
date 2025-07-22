from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def increase_quantity(self):
        self.driver.find_element(By.XPATH, '//button[@aria-label="Increase quantity by one"]//self::span').click()

    def go_to_cart(self):
        self.driver.find_element(By.ID, "nav-cart").click()
