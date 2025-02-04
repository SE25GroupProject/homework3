"""
Module for implementing merge sort algorithm.
"""

import rand

def merge_sort(input_arr):
    """
    Sorts an array using the merge sort algorithm.

    Args:
        input_arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(input_arr) <= 1:
        return input_arr

    half = len(input_arr) // 2

    return recombine(merge_sort(input_arr[:half]), merge_sort(input_arr[half:]))

def recombine(left_arr, right_arr):
    """
    Combines two sorted arrays into one sorted array.

    Args:
        left_arr (list): The left sorted array.
        right_arr (list): The right sorted array.

    Returns:
        list: The combined sorted array.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    while right_index < len(right_arr):
        merge_arr[left_index + right_index] = right_arr[right_index]
        right_index += 1

    while left_index < len(left_arr):
        merge_arr[left_index + right_index] = left_arr[left_index]
        left_index += 1

    return merge_arr

arr = rand.random_array([None] * 20)

print(arr)

arr_out = merge_sort(arr)

print(arr_out)
