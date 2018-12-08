from selenium import webdriver
import logger
import time
import random

from ShopTester import ShopTester
from utils import stringify_links, filter_by_text
import util_excel as utex

# create a WebDriver instance
driver = webdriver.Firefox()

# Navigation Manager
shop = ShopTester(driver)
driver.maximize_window()

# 1) load home page and retrieve section links
home_page = shop.load_home_page()
logger.log("home page", "navigation")

section_links = home_page.section_links
logger.log(stringify_links(section_links), "home_page")

# only now the home page is fully loaded
home_page.screenshot("./sessions/screenshots/homepage.png")

# now select a section for the next step
section_name = "What's New"
section_link = filter_by_text(section_links, section_name)

# 2) load the given section and retrieve item links
section_page = shop.load_section_page(section_link)
subsection_links = section_page.subsection_links

logger.log(stringify_links(subsection_links), "section_page")
section_page.screenshot("./sessions/screenshots/section_page.png")

# now select a subsection for the next step
subsection_name = "Hoodies & Sweatshirts"
subsection_link = filter_by_text(subsection_links, subsection_name)

# 3) load the given sub section and retrieve item links
subsection_page = shop.load_subsection_page(subsection_link)
item_links = subsection_page.item_links

logger.log(stringify_links(item_links), "subsection_page")
subsection_page.screenshot(
    "./sessions/screenshots/subsection_page.png")

# now select an item for the next step
item_name = "Mona Pullover Hoodlie"
item_link = filter_by_text(item_links, item_name, ignore_white_space=True)

# 4) load the given item and add it to the cart
item_page = shop.load_item_page(item_link)

available_colors = item_page.available_color_names
available_sizes = item_page.available_size_names

logger.log("Available colors: {}".format(
    ",".join(available_colors)), "item_page")
logger.log("Available sizes: {}".format(
    ",".join(available_sizes)), "item_page")

item_page.screenshot("./sessions/screenshots/item_page.png")

item_page.pick_color(available_colors[1])
item_page.pick_size(available_sizes[3])

random_nr = random.randint(1, 4)
item_page.pick_quantity(random_nr)
item_page.click_add_to_cart()
time.sleep(3)

# Click on the Checkout box
item_page.click_checkout_box()

# Go to Checkout page
item_page.click_go_to_checkout()

# Go to the next step and fill out the form
first_row = utex.read_shipping_values()[0]
item_page.type_email_address(first_row.user_name)
item_page.type_firstname(first_row.first_name)
item_page.type_lastname(first_row.last_name)
item_page.type_company(first_row.company)
item_page.type_street(first_row.street)
item_page.type_city(first_row.city)
item_page.select_state(first_row.state)
item_page.type_postcode(first_row.postcode)
item_page.select_country(first_row.country_id)
item_page.type_phonenumber(first_row.telephone)

# Select Shipping Method
item_page.click_flat_rate()

# Click Next Button for Review and Payments Page
item_page.click_next_button()
time.sleep(4)

# Place Your Order
item_page.click_place_order_button()
time.sleep(4)

# Take Screenshot of  Your Confirmation Number
item_page.screenshot("./sessions/screenshots/Order_Confirmation.png")
