import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from config import config
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_amazon_purchase(driver):

    driver.get(config.URL)
    driver.implicitly_wait(5)

    home = HomePage(driver)
    search = SearchResultsPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    home.search_product("laptop")
    search.select_products()
    product.increase_quantity()
    product.go_to_cart()
    cart.proceed_to_checkout()
    cart.login(config.EMAIL, config.PASSWORD)

    time.sleep(5)
    driver.quit()
