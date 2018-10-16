from selenium.webdriver.common.by import By

from WebDriverContainer import WebDriverContainer


class ShopSubSectionPage(WebDriverContainer):
    __items_container_selector = (
        By.CSS_SELECTOR, "div.products.wrapper.grid.products-grid")
    __link_selector = (By.CSS_SELECTOR, ".product-item-link")

    def __init__(self, driver):
        super().__init__(driver)

    def get_item_links(self):
        items_container = self._try_find_element(
            self.__items_container_selector, 20)

        links = self._try_find_elements_of(
            items_container, self.__link_selector, 20)

        return links
