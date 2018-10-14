from selenium.webdriver.common.by import By
from WebDriverContainer import WebDriverContainer
from HomePage import HomePage


class ShopTester(WebDriverContainer):
    _home_page_url = "https://shop.polymer-project.org/"

    def __init__(self, driver):
        super().__init__(driver)

    def load_homepage(self):
        self._load_url(self._home_page_url)
        return HomePage(self._driver)
