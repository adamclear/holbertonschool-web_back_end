#!/usr/bin/env python3
''' This function returns the sum of a list of ints and floats. This function
is to be type-annotated. '''

from typing import List, Union


def sum_mixed_list(mxd_lst: List([Union[int, float]])) -> float:
    ''' Returns the sum of the list '''
    return sum(mxd_lst)
