from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="proceedToRetailCheckout"]'))
        ).click()

    def login(self, email, password):
        self.driver.find_element(By.ID, "ap_email_login").send_keys(email)
        self.driver.find_element(By.CLASS_NAME, "a-button-input").click()
        self.driver.find_element(By.ID, "ap_password").send_keys(password)
        self.driver.find_element(By.ID, "signInSubmit").click()
