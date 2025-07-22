import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.amazon.in/")
driver.implicitly_wait(5)


input_text=driver.find_element(By.ID, "twotabsearchtextbox")
input_text.clear()
input_text.send_keys("laptop")

search=driver.find_element(By.ID, "nav-search-submit-button").click()

FIRST_PRODUCT=driver.find_element(By.ID, "a-autoid-1-announce")
FIRST_PRODUCT.click()
SECOND_PRODUCT=driver.find_element(By.ID, "a-autoid-2-announce")
SECOND_PRODUCT.click()

ADD_QUANTITY=driver.find_element(By.XPATH, '//button[@aria-label="Increase quantity by one"]//self::span')
ADD_QUANTITY.click()


GO_TO_CART=driver.find_element(By.ID, "nav-cart")
GO_TO_CART.click()

wait=WebDriverWait(driver, 10)
PROCEED_TO_BUY_BUTTON = wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//input[@name="proceedToRetailCheckout"]')
))
PROCEED_TO_BUY_BUTTON.click()



ENTER_EMAIL=driver.find_element(By.ID, "ap_email_login")
ENTER_EMAIL.send_keys("vj@gmail.com")

CLICK_CONTINUE=driver.find_element(By.CLASS_NAME, "a-button-input").click()

ENTER_PASSWORD=driver.find_element(By.ID, "ap_password")
ENTER_PASSWORD.send_keys("Vj@1234")

driver.find_element(By.ID, "signInSubmit").click()











time.sleep(4)
driver.quit()
    
