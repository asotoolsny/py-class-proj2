from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .HomePage import HomePage
from .WebDriverContainer import WebDriverContainer


class ShopTester(WebDriverContainer):
    _home_page_url = "http://magento2-demo.nexcess.net"
    _search_textbox_selector = (By.NAME, "q")

    def __init__(self, driver):
        super().__init__(driver)

    def load_home_page(self):
        self._load_url(self._home_page_url)
        return HomePage(self._driver)
