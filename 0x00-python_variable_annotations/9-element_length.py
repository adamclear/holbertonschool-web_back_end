#!/usr/bin/env python3
''' Taking a given function and type-annotating it. '''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Returns a list of tuples (i, length of i) from each item in lst '''
    return [(i, len(i)) for i in lst]
