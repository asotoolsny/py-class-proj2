from selenium import webdriver

import logger
from ShopTester import ShopTester
from utils import stringify_links, filter_by_text

# create a WebDriver instance
driver = webdriver.Chrome()
shop = ShopTester(driver)

# 1) load home page and retrieve section links
home_page = shop.load_home_page()
logger.log("home page", "navigation")

# only now the home page is fully loaded
home_page.screenshot("./sessions/screenshots/homepage.png")

# now select a section for the next step
search_results_page = shop.search_item("hoodie")
search_results_page.screenshot(
    "./sessions/screenshots/search_results_page.png")

item_links = search_results_page.item_links
logger.log(stringify_links(item_links), "search_results_page")

# now select an item for the next step
item_link = item_links[0]

# 4) load the given item and add it to the cart
item_page = shop.load_item_page(item_link)

available_colors = item_page.available_color_names
available_sizes = item_page.available_size_names

logger.log("Available colors: {}".format(
    ",".join(available_colors)), "item_page")
logger.log("Available sizes: {}".format(
    ",".join(available_sizes)), "item_page")

item_page.screenshot("./sessions/screenshots/item_page.png")

item_page.pick_color(available_colors[0])
item_page.pick_size(available_sizes[0])
item_page.click_add_to_cart()
