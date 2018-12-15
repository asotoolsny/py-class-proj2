from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .HomePage import HomePage
from .ShopItemPage import ShopItemPage
from .ShopSearchPage import ShopSearchPage
from .ShopSectionPage import ShopSectionPage
from .ShopSubSectionPage import ShopSubSectionPage
from .WebDriverContainer import WebDriverContainer


class ShopTester(WebDriverContainer):
    _home_page_url = "http://magento2-demo.nexcess.net"
    _search_textbox_selector = (By.NAME, "q")

    def __init__(self, driver):
        super().__init__(driver)

    def load_home_page(self):
        self._load_url(self._home_page_url)
        return HomePage(self._driver)

    def load_section_page(self, section_link):
        section_link.click()
        return ShopSectionPage(self._driver)

    def load_subsection_page(self, subsection_link):
        subsection_link.click()
        return ShopSubSectionPage(self._driver)

    def load_item_page(self, item_link):
        item_link.click()
        return ShopItemPage(self._driver)

    def search_item(self, value: str):
        search_textbox = self._try_find_element(
            self._search_textbox_selector, 20)
        search_textbox.clear()
        search_textbox.send_keys(value)
        search_textbox.send_keys(Keys.ENTER)

        return ShopSearchPage(self._driver)
