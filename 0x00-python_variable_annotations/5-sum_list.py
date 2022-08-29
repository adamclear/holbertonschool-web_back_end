#!/usr/bin/env python3
''' This function returns the sum of a list of floats. This function is to
be type annotated. '''

from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' Returns the sum of the list '''
    return sum(input_list)
