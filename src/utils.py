from typing import List, Type, Iterable, Any
from selenium.webdriver.remote.webelement import WebElement


def print_links(links: List[Any]):
    for link in links:
        print(link.text.strip())


def find_element_by_title(elements, search_text, ignore_case=True, ignore_white_space=False):
    return filter_by_attr(elements, "option-label", search_text, ignore_case, ignore_white_space)


def find_element_by_text(elements, search_text, ignore_case=True, ignore_white_space=False):
    return filter_by_text(elements, search_text, ignore_case, ignore_white_space)


def filter_by_attr(elements, attr, search_text, ignore_case=True, ignore_white_space=False):
    for element in elements:
        if are_strings_equal(element.get_attribute(attr), search_text, ignore_case, ignore_white_space):
            return element

    return None


def filter_by_text(elements, search_text: str, ignore_case=True, ignore_white_space=False):
    for element in elements:
        if are_strings_equal(element.text, search_text, ignore_case, ignore_white_space):
            return element

    return None


def are_strings_equal(first: str, second: str, ignore_case=True, ignore_white_space=False):
    """
    Compares two strings.

    :Args:
        - first - The first string argument.
        - second - The second string argument.
        - ignore_case - A flag to ignore case.
        - ignore_white_space - A flag to ignore whitespace.

    :Returns:
        - Boolean value - if two strings are equal

    :Usage:
        if are_strings_equal("string", "String ", ignore_case=True, ignore_white_space=True) 
    """

    if ignore_case:
        first = first.lower()
        second = second.lower()

    if ignore_white_space:
        first = first.strip()
        second = second.strip()

    return first == second
