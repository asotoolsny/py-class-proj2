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

    def tearDown(self):
        self.__shop._close()


if __name__ == "__main__":
    unittest.main()
