import unittest

from selenium import webdriver

import logger
from ShopTester import ShopTester
from utils import filter_by_text, stringify_links


class TestHomePageSections(unittest.TestCase):
    def setUp(self):
        self.__driver = webdriver.Firefox()
        self.__shop = ShopTester(self.__driver)

    def test_if_has_sections(self):
        home_page = self.__shop.load_home_page()
        section_links = home_page.section_links
        assert section_links

        # assert section_links has a section named "What's new"
        section_name = "What's New"
        section_link = filter_by_text(section_links, section_name)
        assert section_link

        # 2) load the given section and retrieve item links
        section_page = self.__shop.load_section_page(section_link)
        subsection_links = section_page.subsection_links
        assert subsection_links

        # now select a subsection for the next step
        subsection_name = "Hoodies & Sweatshirts"
        subsection_link = filter_by_text(subsection_links, subsection_name)
        assert subsection_link

        # 3) load the given sub section and retrieve item links
        subsection_page = self.__shop.load_subsection_page(subsection_link)
        item_links = subsection_page.item_links
        assert item_links

        # now select an item for the next step
        item_name = "Mona Pullover Hoodlie"
        item_link = filter_by_text(
            item_links, item_name, ignore_white_space=True)
        assert item_link

        # 4) load the given item and add it to the cart
        item_page = self.__shop.load_item_page(item_link)

        available_colors = item_page.available_color_names
        available_sizes = item_page.available_size_names

        assert available_colors
        item_page.pick_color(available_colors[0])

        assert available_sizes
        item_page.pick_size(available_sizes[-1])

        item_page.pick_quantity(2)
        item_page.click_add_to_cart()

    def tearDown(self):
        self.__shop._close()


if __name__ == "__main__":
    unittest.main()
