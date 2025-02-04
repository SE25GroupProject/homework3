"""Test file for merge sort. Tests on an empty array, an array with one item, and a large array."""

import hw2_debugging
import rand

def test_empty_array():
    """Check to make sure the merge sort function can take a random array and not break."""
    empty_arr = []

    returned_arr = hw2_debugging.merge_sort(empty_arr)

    assert returned_arr == []

def test_single_digit_array():
    """Check that merge sort can handle an array with a single digit"""
    single_arr = rand.random_array([None] )

    returned_arr = hw2_debugging.merge_sort(single_arr)

    assert returned_arr == single_arr

def test_large_array():
    """Check merge sort works on an array with a large number of items"""
    large_arr = rand.random_array([None] * 200000)

    returned_arr = hw2_debugging.merge_sort(large_arr)

    for idx, num in enumerate(returned_arr):
        if idx != len(returned_arr) - 1:
            assert num <= returned_arr[idx + 1]
