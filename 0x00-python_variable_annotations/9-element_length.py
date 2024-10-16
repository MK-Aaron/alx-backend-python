#!/usr/bin/env python3
"""
Duck type and iterable objects
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns lentgh of list
    """
    return [(i, len(i)) for i in lst]
