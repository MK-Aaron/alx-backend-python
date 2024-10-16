#!/usr/bin/env python3
"""
Complex types - mixed list
"""
from typing import List

def sum_mixed_list(mxd_lst: List[float, int]) -> float:
    """
    finds sums in a list and return a float
    """
    return sum(mxd_lst)
