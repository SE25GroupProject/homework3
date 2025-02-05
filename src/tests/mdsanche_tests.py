import pytest
import hw2_debugging

def test_merge_sort_empty_array():
    """
    Test merge_sort with an empty array.
    """
    input_arr = []
    expected_output = []
    assert merge_sort(input_arr) == expected_output

def test_merge_sort_single_element_array():
    """
    Test merge_sort with a single-element array.
    """
    input_arr = [42]
    expected_output = [42]
    assert merge_sort(input_arr) == expected_output

def test_merge_sort_random_array():
    """
    Test merge_sort with a randomly shuffled array.
    """
    input_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected_output = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert merge_sort(input_arr) == expected_output