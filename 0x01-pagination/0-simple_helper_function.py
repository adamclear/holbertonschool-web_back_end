#!/usr/bin/env python3
''' This module contains the index_range function. '''
import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    ''' This function should return a tuple of size two containing
    a start index and an end index corresponding to the range
    of indexes to return in a list for those particular pagination
    parameters. '''
    return (page - 1) * page_size, page_size * page
