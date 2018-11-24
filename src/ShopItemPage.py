from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from utils import filter_by_attr
from WebDriverContainer import WebDriverContainer
import util_excel as utex


class ShopItemPageModel(WebDriverContainer):
    """It will contain all Selenium related scripts"""

    __color_container_selector = (By.CSS_SELECTOR, ".swatch-attribute.color")
    __color_option_selector = (By.CSS_SELECTOR, ".swatch-option.color")

    __size_container_selector = (By.CSS_SELECTOR, ".swatch-attribute.size")
    __size_option_selector = (By.CSS_SELECTOR, ".swatch-option.text")

    __quantity_selector = (By.CSS_SELECTOR, "input#qty")

    __btn_add_to_cart_selector = (By.CSS_SELECTOR, "#product-addtocart-button")

    # Checkout box
    __checkout_box_selector = (By.CSS_SELECTOR, "a.action.showcart")
    __go_to_checkout_selector = (
        By.CSS_SELECTOR, "button#top-cart-btn-checkout")

    # Shipping Address Information
    __email_selector = (By.CSS_SELECTOR, "#customer-email")
    __firstname_selector = (By.CSS_SELECTOR, "[name='firstname']")
    __lastname_selector = (By.CSS_SELECTOR, "[name='lastname']")
    __company_selector = (By.CSS_SELECTOR, "[name='company']")
    __street_selector = (By.CSS_SELECTOR, "[name='street[0]']")
    __city_selector = (By.CSS_SELECTOR, "[name='city']")
    __state_selector = (By.CSS_SELECTOR, "[name='region_id']")
    __postcode_selector = (By.CSS_SELECTOR, "[name='postcode']")
    __country_selector = (By.CSS_SELECTOR, "[name='country_id']")
    __phone_number_selector = (By.CSS_SELECTOR, "[name='telephone']")

    # Shipping Methods
    __flatrate_selector = (By.CSS_SELECTOR, "#s_method_flatrate_flatrate")
    __table_rate_selector = (By.CSS_SELECTOR, "#s_method_tablerate_bestway")

    # Next Button
    __next_button_selector = (By.CSS_SELECTOR, ".button")

    # Place Order Button
    __place_order_button_selector = (By.CSS_SELECTOR, "[title='Place Order']")

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
    def quantity(self):
        return self._try_find_element(self.__quantity_selector, 20)

    @property
    def btn_add_to_cart(self):
        return self._try_find_element(self.__btn_add_to_cart_selector, 20)

    @property
    def checkout_box(self):
        return self._try_find_element(self.__checkout_box_selector, 20)

    @property
    def go_to_checkout(self):
        return self._try_find_element(self.__go_to_checkout_selector, 20)

    # Shipping Address Information
    @property
    def email_adder(self):
        return self._try_find_element(self.__email_selector, 20)

    @property
    def firstname_adder(self):
        return self._try_find_element(self.__firstname_selector, 20)

    @property
    def lastname_adder(self):
        return self._try_find_element(self.__lastname_selector, 20)

    @property
    def company_adder(self):
        return self._try_find_element(self.__company_selector, 20)

    @property
    def street_adder(self):
        return self._try_find_element(self.__street_selector, 20)

    @property
    def city_adder(self):
        return self._try_find_element(self.__city_selector, 20)

    @property
    def state_adder(self):
        return self._try_find_element(self.__state_selector, 20)

    @property
    def postcode_adder(self):
        return self._try_find_element(self.__postcode_selector, 20)

    @property
    def country_adder(self):
        return self._try_find_element(self.__country_selector, 20)

    @property
    def phonenumber_adder(self):
        return self._try_find_element(self.__phone_number_selector, 20)

    # Shipping Method
    @property
    def flat_rate(self):
        return self._try_find_element(self.__flatrate_selector, 20)

    @property
    def table_rate(self):
        return self._try_find_element(self.__table_rate_selector, 20)

    # Next Button
    @property
    def next_button(self):
        return self._try_find_element(self.__next_button_selector, 20)

    # Review & Payment --> Place Order Button
    @property
    def place_order_button(self):
        return self._try_find_element(self.__place_order_button_selector, 20)


class ShopItemPage(WebDriverContainer):
    __title_attr__ = "option-label"
    __rating_attr__ = "title"

    def __init__(self, driver):
        super().__init__(driver)
        self.__page__ = ShopItemPageModel(driver)

    @property
    def available_color_names(self):
        colors = []
        for color_option in self.__page__.available_colors:
            colors.append(color_option.get_attribute(self.__title_attr__))

        return colors

    @property
    def available_size_names(self):
        sizes = []
        for size_option in self.__page__.available_sizes:
            sizes.append(size_option.get_attribute(self.__title_attr__))

        return sizes

    def pick_color(self, color):
        selected_color_option = filter_by_attr(
            self.__page__.available_colors, self.__title_attr__, color)
        selected_color_option.click()
        print("Color is picked")

    def pick_size(self, size):
        selected_size_option = filter_by_attr(
            self.__page__.available_sizes, self.__title_attr__, size)
        selected_size_option.click()
        print("Size is picked")

    def pick_quantity(self, quantity):
        quantity_textbox = self.__page__.quantity
        quantity_textbox.clear()
        quantity_textbox.send_keys(str(quantity))
        print("Qty is picked")

    def pick_quantity(self, quantity):
        quantity_textbox = self.__page__.quantity
        quantity_textbox.clear()
        quantity_textbox.send_keys(str(quantity))

    def click_add_to_cart(self):
        self.__page__.btn_add_to_cart.click()
        print("Added to the cart")

    def click_checkout_box(self):
        click_checkbox = self.__page__.checkout_box
        click_checkbox.click()

    def click_go_to_checkout(self):
        click_go_to_checkout = self.__page__.go_to_checkout
        click_go_to_checkout.click()

    def type_email_address(self, email_address):
        email_typing = self.__page__.email_adder
        email_typing.clear()
        email_typing.send_keys(str(email_address))

    def type_firstname(self, first_name):
        firstname_typing = self.__page__.firstname_adder
        firstname_typing.clear()
        firstname_typing.send_keys(str(first_name))

    def type_lastname(self, last_name):
        lastname_typing = self.__page__.lastname_adder
        lastname_typing.clear()
        lastname_typing.send_keys(str(last_name))

    def type_company(self, company_name):
        company_typing = self.__page__.company_adder
        company_typing.clear()
        company_typing.send_keys(str(company_name))

    def type_street(self, street_name):
        street_typing = self.__page__.street_adder
        street_typing.clear()
        street_typing.send_keys(str(street_name))

    def type_city(self, city_name):
        city_typing = self.__page__.city_adder
        city_typing.clear()
        city_typing.send_keys(str(city_name))

    def select_state(self, state_name):
        state_selecting = self.__page__.state_adder
        sel_state = Select(state_selecting)
        sel_state.select_by_visible_text(state_name)

    def type_postcode(self, postcode_number):
        postcode_typing = self.__page__.postcode_adder
        postcode_typing.clear()
        postcode_typing.send_keys(postcode_number)

    def select_country(self, country_name):
        country_selecting = self.__page__.country_adder
        sel_country = Select(country_selecting)
        sel_country.select_by_visible_text(country_name)

    def type_phonenumber(self, phone_number):
        phonenumber_typing = self.__page__.phonenumber_adder
        phonenumber_typing.clear()
        phonenumber_typing.send_keys(phone_number)

    def click_flat_rate(self):
        clicking_flatrate = self.__page__.flat_rate
        clicking_flatrate.click()

    def click_table_rate(self):
        clicking_tablerate = self.__page__.table_rate
        clicking_tablerate.click()

    def click_next_button(self):
        clicking_next_button = self.__page__.next_button
        clicking_next_button.click()

    def click_place_order_button(self):
        clicking_place_order = self.__page__.place_order_button
        clicking_place_order.click()
