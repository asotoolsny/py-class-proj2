from selenium.webdriver.common.by import By

from WebDriverContainer import WebDriverContainer


class HomePage(WebDriverContainer):
    __page_container_selector = (By.CLASS_NAME, "navigation")
    __link_selector = (By.CSS_SELECTOR, "li.level0.ui-menu-item")

    def __init__(self, driver):
        super().__init__(driver)

    def get_section_links(self):
        """will return link web elements of sections."""
        page_container = self._try_find_element(
            self.__page_container_selector, 20)

        links = self._try_find_elements_of(
            page_container, self.__link_selector, 20)

        return links
