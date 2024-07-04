#!/usr/bin/env python3
"""type-annotated function"""
import math
from typing import List


def sum_list(input_list: List[float]) -> float:
  """takes a list input_list of floats and returns their sum as a float"""
    return sum(input_list)
