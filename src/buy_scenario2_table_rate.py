from selenium import webdriver
import logger
import time
import random

from ShopTester import ShopTester
from utils import stringify_links, filter_by_text
import util_excel as utex

# Create a webdriver instance
driver = webdriver.Chrome()
driver.maximize_window()

# Navigation Manger
shop = ShopTester(driver)

# 1) Load homepage and retrieve section links
home_page = shop.load_home_page()
section_links = home_page.section_links
home_page.screenshot("./sessions/screenshots/homepage_tableRate.png")

# Select a section
section_name = "Gear"
section_link = filter_by_text(section_links, section_name)

# 2) load the given section and retrieve item links
section_page = shop.load_section_page(section_link)
subsection_links = section_page.subsection_links

# Now select a sub section
subsection_name = "Bags"
subsection_link = filter_by_text(subsection_links, subsection_name)

# 3) Load the given subsection and retrieve item links
subsection_page = shop.load_subsection_page(subsection_link)
item_links = subsection_page.item_links

# Now select an item from the items link by Text
item_name = "Crown Summit Backpack"
item_link = filter_by_text(item_links, item_name)

# 4) Load the given item and add it to the cart
item_page = shop.load_item_page(item_link)

item_page.screenshot("./sessions/screenshots/itempage_tableRate.png")

random_nr = random.randint(1, 9)
item_page.pick_quantity(random_nr)
item_page.click_add_to_cart()
item_page.click_checkout_box()
item_page.click_go_to_checkout()

# Go to the next step and fill out the form
first_row = utex.read_shipping_values()[0]
item_page.type_email_address(first_row["username"])
item_page.type_firstname(first_row["firstname"])
item_page.type_lastname(first_row["lastname"])
item_page.type_company(first_row["company"])
item_page.type_street(first_row["street"])
item_page.type_city(first_row["city"])
item_page.select_state(first_row["state"])
item_page.type_postcode(first_row["postcode"])
item_page.select_country(first_row["country_id"])
item_page.type_phonenumber(first_row["telephone"])

# Select Shipping Method
item_page.click_table_rate()

# Click Next Button for Review and Payments Page
item_page.click_next_button()
time.sleep(4)

# Place Your Order
item_page.click_place_order_button()
time.sleep(4)

# Take Screenshot of  Your Confirmation Number
item_page.screenshot(
    "./sessions/screenshots/Order_Confirmation_table_rate.png")
