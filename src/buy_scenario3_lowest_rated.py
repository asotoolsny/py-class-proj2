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
driver = webdriver.Chrome(executable_path="/Users/ersekrem/Documents/ClassAso/chromedriver")

sleep = time.sleep(3)

baseURL = "http://magento2-demo.nexcess.net/"
driver.get(baseURL)

menu_section = "Gear"
driver.find_element_by_link_text(menu_section).click()

menu_subsection = "Watches"
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

current_min_number = items_rating[0]
for number in items_rating:
        if number < current_min_number:
                current_min_number = number
print("The lowest rated item: ", current_min_number)

if min(items_rating) == current_min_number:
        print("Found the lowest rated item : ", current_min_number, dict1[current_min_number])
        lowest_rated_item_locator = driver.find_element(By.LINK_TEXT, dict1[current_min_number])
        lowest_rated_item_locator.click()
        print("Lowest rated item is selected!")
        driver.save_screenshot("./py-class-proj2-master/screenshots/lowest_item.png")
        sleep

# Type Quantity
quantity_locator = driver.find_element_by_id("qty")
quantity_locator.clear()
random_nr = random.randint(1,5)
quantity_locator.send_keys(random_nr)
print("Quantity is added")
sleep

# Click Add to Cart
add_to_cart_locator = driver.find_element_by_id("product-addtocart-button")
add_to_cart_locator.click()
print("Item is sent to the Shopping Cart")
sleep

# Click Checkout Box
checkout_box_selector = (By.CSS_SELECTOR, "a.action.showcart")
checkout_box_locator = driver.find_element(checkout_box_selector)
checkout_box_locator.click()
sleep

# Click Go to Checkout    
go_to_checkout_selector = (By.CSS_SELECTOR, "button#top-cart-btn-checkout")
go_to_checkout_locator = driver.find_element(go_to_checkout_selector)
go_to_checkout_locator.click()
