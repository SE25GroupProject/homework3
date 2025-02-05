"""
Module for generating random arrays.
"""

import random

def random_array(arr):
    """
    Fills an array with random integers between 1 and 20.

    Args:
        arr (list): The array to be filled with random integers.

    Returns:
        list: The array filled with random integers.
    """
    for i, _ in enumerate(arr):
        arr[i] = random.randint(1, 20)
    return arr
