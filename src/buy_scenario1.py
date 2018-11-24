from selenium import webdriver

import logger
from ShopTester import ShopTester
from utils import stringify_links, filter_by_text

# create a WebDriver instance
driver = webdriver.Firefox()
shop = ShopTester(driver)

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
subsection_page.screenshot("./sessions/screenshots/subsection_page.png")

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

item_page.pick_color(available_colors[0])
item_page.pick_size(available_sizes[-1])
item_page.pick_quantity(2)
item_page.click_add_to_cart()
