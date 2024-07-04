#!/usr/bin/env python3
"""
module provides Safely retrieves the value for a given key in a mapping
"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    This function Safely retrieves a value from a dictionary.

    Parameters:
    - dct (Mapping): The dictionary to retrieve values from.
    - key (Any): The key to look up in the dictionary.
    - default (Union[T, None]): The default value to return if the key is not found (default is None).

    Returns:
    - Union[T, None]: The value corresponding to the key in the dictionary, or the default value if key is not found.
    """

    if key in dct:
        return dct[key]
    else:
        return default
