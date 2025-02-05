"""The file that helps create an array of numbers with values from 1 to 20."""

import random

def random_array(arr):
    """takes in an empty array and fills it with random numbers from 1 to 20"""
    for item in enumerate(arr):
        i = item[0]
        arr[i] = random.randint(1, 20)
    return arr