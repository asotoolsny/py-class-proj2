from selenium.webdriver.common.by import By
from WebDriverContainer import WebDriverContainer


class HomePage(WebDriverContainer):
    _shop_sections_container_selector = (By.CLASS_NAME, "shop-tabs")
    _shop_section_link_selector = (By.CSS_SELECTOR, "a")

    def __init__(self, driver):
        super().__init__(driver)

    def get_section_links(self):
        tab_container = self._try_find_element(
            self._shop_sections_container_selector, 20)

        # should find below section links
        # Men's Outerwear | Ladies Outerwear | Men's T-Shirts | Ladies T-Shirts
        section_links = self._try_find_elements_of(
            tab_container, self._shop_section_link_selector, 20)

        return section_links
