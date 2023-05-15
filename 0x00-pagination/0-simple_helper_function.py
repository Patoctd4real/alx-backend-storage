#!/usr/bin/env python3
"""a function named index_range that takes
two integer arguments page and page_size.
"""


def index_range(page: int, page_size: int) -> tuple:
    """tuple containing page and the page_size """

    opening_index = (page - 1) * page_size
    closing_index = opening_index + page_size
    return (opening_index, closing_index)
