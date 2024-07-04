#!/usr/bin/env python3
"""type-annotated function"""
from typing import Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, type(None)]:
    """correct duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
