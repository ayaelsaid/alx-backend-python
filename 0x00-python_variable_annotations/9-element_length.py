#!/usr/bin/env python3
"""Annotate the below function’s parameters"""    
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples of sequence and int"""
    return [(i, len(i)) for i, _ in lst]
