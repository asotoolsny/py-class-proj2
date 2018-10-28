from selenium.webdriver.common.by import By

from WebDriverContainer import WebDriverContainer


class ShopSearchPageModel(WebDriverContainer):
    __items_container_selector = (
        By.CSS_SELECTOR, "div.products.wrapper.grid.products-grid")
    __link_selector = (By.CSS_SELECTOR, ".product-item-link")

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def item_links(self):
        items_container = self._try_find_element(
            self.__items_container_selector, 20)

        links = self._try_find_elements_of(
            items_container, self.__link_selector, 20)

        return links


class ShopSearchPage(WebDriverContainer):
    def __init__(self, driver):
        super().__init__(driver)
        self.__page__ = ShopSearchPageModel(driver)

    @property
    def item_links(self):
        return self.__page__.item_links
