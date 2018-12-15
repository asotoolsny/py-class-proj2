from typing import Any, Iterable, List, Type

from selenium.webdriver.remote.webelement import WebElement


def stringify_links(links: List[Any]):
    tuples = []
    for link in links:
        link_tuple = (link.text.strip(), link.get_attribute("href"))
        tuples.append(link_tuple)

    def stringify_link(link_tuple):
        return "({}: {})".format(link_tuple[0], link_tuple[1])

    return ",".join(list(map(stringify_link, tuples)))


def filter_by_text(elements: List[Any], search_text: str, ignore_case=True, ignore_white_space=False):
    return filter_by(elements, lambda element: element.text, search_text, ignore_case, ignore_white_space)


def filter_by_attr(elements: List[Any], attr: str, search_text: str, ignore_case=True, ignore_white_space=False):
    return filter_by(elements, lambda element: element.get_attribute(attr), search_text, ignore_case, ignore_white_space)


def filter_by(elements: List[Any], el_mapper, search_text: str, ignore_case=True, ignore_white_space=False):
    for element in elements:
        if are_strings_equal(el_mapper(element), search_text, ignore_case, ignore_white_space):
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
