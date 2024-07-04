#!/usr/bin/env python3
"""module provides Safely retrieves the value for a given key in a mapping"""
from typing import Union, Mapping, Any, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[T, Any]:
    """
    Safely retrieves the value for a given key in a mapping,
    or returns a default value if the key is not present.

    Parameters:
    dct (Mapping): The mapping to retrieve the value from.
    key (Any): The key whose value to retrieve.
    default (Union[T, None]): The default value to return if the key is not found.

    Returns:
    Union[T, Any]: The value corresponding to the key if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
