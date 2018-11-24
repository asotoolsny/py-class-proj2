from selenium import webdriver
from selenium.webdriver.common.by import By
import logger
import time
import random
from selenium.common import exceptions

from ShopTester import ShopTester
from utils import stringify_links, filter_by_text
import util_excel as utex
import ShopItemPage 

# Create a webdriver instance
driver = webdriver.Chrome()
driver.maximize_window()

sleep = time.sleep(5)

baseURL = "http://magento2-demo.nexcess.net/"
driver.get(baseURL)

menu_section = "What's New"
driver.find_element_by_link_text(menu_section).click()

menu_subsection = "Bras & Tanks"
driver.find_element_by_link_text(menu_subsection).click()

# Find the highest rated item in the section and select the item. 
items = driver.find_elements(By.CSS_SELECTOR, "[class = 'item product product-item']")

items_rating = []
dict1 = {}
for item in items:
        try:
                item_name_locator = item.find_element_by_css_selector("[class = 'product-item-link']")
                item_name = item_name_locator.text
                print(item_name)
                item_rating = item.find_element_by_css_selector("[class = 'rating-result']").get_attribute("title")
                # Add keys(item rating) and values(item name) 
                dict1[item_rating]=item_name
                items_rating.append(item_rating)
                print(item_rating)
        except exceptions.NoSuchElementException:
                print("---NOT RATED YET!---")

current_max_number = items_rating[0]
for number in items_rating:
        if number > current_max_number:
                current_max_number = number
print("The highest rated item: ", current_max_number)

if max(items_rating) == current_max_number:
        print("Found the highest rated item : ", current_max_number, dict1[current_max_number] )
        highest_rated_item_locator = driver.find_element(By.LINK_TEXT, dict1[current_max_number])
        highest_rated_item_locator.click()
        print("Highest rated item is selected!")
        driver.save_screenshot("C:\PythonClass/py-class-proj2-master/screenshots/highest_item.png")
        sleep

# #Select Color
# color_locator = driver.find_element(By.CSS_SELECTOR, "[option-label = 'Black']")
# color_locator.click()
# print("Color is selected!")
# sleep

# #Select Size
# size_locator = driver.find_element(By.CSS_SELECTOR, "[option-id='168']")
# size_locator.click()

# # Type Quantity
# quantity_locator = driver.find_element_by_id("qty")
# quantity_locator.clear()
# random_nr = random.randint(1,5)
# quantity_locator.send_keys(random_nr)
# print("Quantity is added")
# sleep

# # Click Add to Cart
# add_to_cart_locator = driver.find_element_by_id("product-addtocart-button")
# add_to_cart_locator.click()
# print("Item is sent to the Shopping Cart")
# sleep

# # Click Checkout Box
# checkout_box_selector = (By.CSS_SELECTOR, "a.action.showcart")
# checkout_box_locator = driver.find_element(checkout_box_selector)
# checkout_box_locator.click()
# sleep

# # Click Go to Checkout    
# go_to_checkout_selector = (By.CSS_SELECTOR, "button#top-cart-btn-checkout")
# go_to_checkout_locator = driver.find_element(go_to_checkout_selector)
# go_to_checkout_locator.click()
