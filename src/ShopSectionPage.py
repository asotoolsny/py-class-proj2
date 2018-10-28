from selenium.webdriver.common.by import By

from WebDriverContainer import WebDriverContainer


class ShopSectionPageModel(WebDriverContainer):
    __sidebar_container_selector = (By.CSS_SELECTOR, ".sidebar.sidebar-main")
    __link_selector = (By.CSS_SELECTOR, "ul.items > li.item > a")

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def subsection_links(self):
        sidebar_container = self._try_find_element(
            self.__sidebar_container_selector, 20)

        links = self._try_find_elements_of(
            sidebar_container, self.__link_selector, 20)

        return links


class ShopSectionPage(WebDriverContainer):
    def __init__(self, driver):
        super().__init__(driver)
        self.__page__ = ShopSectionPageModel(driver)

    @property
    def subsection_links(self):
        return self.__page__.subsection_links
