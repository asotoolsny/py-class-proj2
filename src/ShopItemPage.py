from selenium.webdriver.common.by import By

from WebDriverContainer import WebDriverContainer
from utils import find_element_by_title_ignore_case


class ShopItemPage(WebDriverContainer):
    __color_container_selector = (By.CSS_SELECTOR, ".swatch-attribute.color")
    __color_option_selector = (By.CSS_SELECTOR, ".swatch-option.color")

    __size_container_selector = (By.CSS_SELECTOR, ".swatch-attribute.size")
    __size_option_selector = (By.CSS_SELECTOR, ".swatch-option.text")

    __btn_add_to_cart_selector = (By.CSS_SELECTOR, "#product-addtocart-button")

    def __init__(self, driver):
        super().__init__(driver)

    def add_to_cart(self, color, size):
        color_container = self._try_find_element(
            self.__color_container_selector, 20)
        color_options = self._try_find_elements_of(
            color_container, self.__color_option_selector, 20)
        selected_color_option = find_element_by_title_ignore_case(
            color_options, color)
        selected_color_option.click()

        size_container = self._try_find_element(
            self.__size_container_selector, 20)
        size_options = self._try_find_elements_of(
            size_container, self.__size_option_selector, 20)
        selected_size_option = find_element_by_title_ignore_case(
            size_options, size)
        selected_size_option.click()

        btn_add_to_cart = self._try_find_element(
            self.__btn_add_to_cart_selector, 20)

        btn_add_to_cart.click()
