from selenium import webdriver

from ShopTester import ShopTester
from utils import filter_by_text

# create a WebDriver instance
driver = webdriver.Chrome()
shop = ShopTester(driver)

# 1) load home page and retrieve section links
home_page = shop.load_home_page()
section_links = home_page.get_section_links()

# now select a section for the next step
section_name = "What's New"
section_link = filter_by_text(section_links, section_name)

# 2) load the given section and retrieve item links
section_page = shop.load_section_page(section_link)
subsection_links = section_page.get_subsection_links()

# now select a subsection for the next step
subsection_name = "Hoodies & Sweatshirts"
subsection_link = filter_by_text(subsection_links, subsection_name)

# 3) load the given sub section and retrieve item links
subsection_page = shop.load_subsection_page(subsection_link)
item_links = subsection_page.get_item_links()

# now select an item for the next step
item_name = "Mona Pullover Hoodlie"
item_link = filter_by_text(item_links, item_name, ignore_white_space=True)

# 4) load the given item and add it to the cart
item_page = shop.load_item_page(item_link)

available_colors = item_page.available_color_names
available_sizes = item_page.available_size_names

item_page.pick_color(available_colors[0])
item_page.pick_size(available_sizes[0])
item_page.click_add_to_cart()
