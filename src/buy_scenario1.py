from selenium import webdriver
from ShopTester import ShopTester

driver = webdriver.Firefox()
tester = ShopTester(driver)

home_page_tester = tester.load_homepage()

for link in home_page_tester.get_section_links():
    print(link.text)
