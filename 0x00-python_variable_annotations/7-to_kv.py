#!/usr/bin/env python3
''' This function returns a tuple of a string and float from a given string and
int/float. This function is to be type-annotated '''

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' Returns a tuple of k, v as a str and float '''
    return k, v ** 2
