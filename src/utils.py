def print_links(links):
    for link in links:
        print(link.text.strip())


def find_element_by_title_ignore_case(elements, search_text, ignore_case=True, ignore_white_space=False):
    if ignore_case:
        search_text = search_text.lower()

    if ignore_white_space:
        search_text = search_text.strip()

    return next(x for x in elements if str(x.get_attribute("option-label")).lower() == search_text)


def find_element_by_text(elements, search_text, ignore_case=True, ignore_white_space=False):
    if ignore_case:
        search_text = search_text.lower()

    if ignore_white_space:
        search_text = search_text.strip()

    return next(x for x in elements if str(x.text).lower() == search_text)
