from selenium import webdriver

from shop.ShopTester import ShopTester

# create a WebDriver instance
driver = webdriver.Chrome()
shop = ShopTester(driver)

# 1) load home page and retrieve section links
home_page = shop.load_home_page()
