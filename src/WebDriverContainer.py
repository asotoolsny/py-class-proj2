import typing

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class WebDriverContainer():
    def __init__(self, driver):
        self._driver = driver

    def screenshot(self, path: str):
        self._driver.save_screenshot(path)

    def _load_url(self, url: str):
        self._driver.get(url)

    def _try_find_element(self, by_query, timeout=10):
        """will try to find element or will wait until it appeared on the page."""
        return self.__wait_until(self._driver, expected_conditions.presence_of_element_located(by_query), timeout)

    def _try_find_elements(self, by_query, timeout=10):
        """will try find all elements or will wait until they appeared on the page."""
        return self.__wait_until(self._driver, expected_conditions.presence_of_all_elements_located(by_query), timeout)

    def _try_find_element_of(self, parent, by_query, timeout=10):
        """will try find element or will wait until it appeared on the page."""
        return self.__wait_until(parent, expected_conditions.presence_of_element_located(by_query), timeout)

    def _try_find_elements_of(self, parent, by_query, timeout=10):
        """will try find all elements or will wait until they appeared on the page."""
        return self.__wait_until(parent, expected_conditions.presence_of_all_elements_located(by_query), timeout)

    def _close(self):
        self._driver.close()

    def __wait_until(self, container, condition, timeout=10):
        waiter = WebDriverWait(container,
                               timeout,
                               poll_frequency=1,
                               ignored_exceptions=[NoSuchElementException,
                                                   ElementNotVisibleException,
                                                   ElementNotSelectableException])

        return waiter.until(condition)
