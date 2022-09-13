#!/usr/bin/env python3
''' This module contains the Server class. '''
import csv
import math
from typing import Any, Dict, List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' Finds the correct indexes to paginate the dataset correctly
        and return the appropriate page of the dataset. '''
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        return self.dataset()[
            index_range(page, page_size)[0]:index_range(page, page_size)[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        ''' Returns a dictionary containing pagination info. '''
        return {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if (page + 1) * page_size <
            len(self.dataset()) else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': math.floor(len(self.dataset()) / page_size)
        }
