import unittest

from selenium import webdriver

import logger
from ShopTester import ShopTester
from utils import filter_by_text, stringify_links


class TestHomePageSections(unittest.TestCase):
    def test_if_has_sections(self):
        driver = webdriver.Firefox()
        shop = ShopTester(driver)

        home_page = shop.load_home_page()

        section_links = home_page.section_links
        self.assertIsNotNone(section_links)

        shop._close()

if __name__ == "__main__":
    unittest.main()
