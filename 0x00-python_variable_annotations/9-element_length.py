#!/usr/bin/env python3
"""type-annotated function"""    
from typing import List, Tuple, Sequence


def element_length(lst: List[Tuple[Sequence, int]]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples of sequence and int"""
    return [(i, len(i)) for i, _ in lst]
