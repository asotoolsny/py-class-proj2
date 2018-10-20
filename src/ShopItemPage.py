from selenium.webdriver.common.by import By

from WebDriverContainer import WebDriverContainer
from utils import find_element_by_title


class ShopItemPageModel(WebDriverContainer):
    __color_container_selector = (By.CSS_SELECTOR, ".swatch-attribute.color")
    __color_option_selector = (By.CSS_SELECTOR, ".swatch-option.color")

    __size_container_selector = (By.CSS_SELECTOR, ".swatch-attribute.size")
    __size_option_selector = (By.CSS_SELECTOR, ".swatch-option.text")

    __btn_add_to_cart_selector = (By.CSS_SELECTOR, "#product-addtocart-button")

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def available_colors(self):
        color_container = self._try_find_element(
            self.__color_container_selector, 20)
        color_options = self._try_find_elements_of(
            color_container, self.__color_option_selector, 20)

        return color_options

    @property
    def available_sizes(self):
        size_container = self._try_find_element(
            self.__size_container_selector, 20)
        size_options = self._try_find_elements_of(
            size_container, self.__size_option_selector, 20)

        return size_options

    @property
    def btn_add_to_cart(self):
        return self._try_find_element(
            self.__btn_add_to_cart_selector, 20)


class ShopItemPage(WebDriverContainer):
    def __init__(self, driver):
        super().__init__(driver)
        self.__page = ShopItemPageModel(driver)

    @property
    def available_color_names(self):
        colors = []
        for color_option in self.__page.available_colors:
            colors.append(color_option.get_attribute("option-label"))

        return colors

    @property
    def available_size_names(self):
        sizes = []
        for size_option in self.__page.available_sizes:
            sizes.append(size_option.get_attribute("option-label"))

        return sizes

    def pick_color(self, color):
        selected_color_option = find_element_by_title(
            self.__page.available_colors, color)
        selected_color_option.click()

    def pick_size(self, size):
        selected_size_option = find_element_by_title(
            self.__page.available_sizes, size)
        selected_size_option.click()

    def click_add_to_cart(self):
        self.__page.btn_add_to_cart.click()
