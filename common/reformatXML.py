def remove_empty_elements(element):
    for child in list(element):
        remove_empty_elements(child)
        if child.text is None and len(child) == 0:
            element.remove(child)
    if element.text is None and len(element) == 0:
        parent = element.find("..")
        if parent is not None:
            parent.remove(element)