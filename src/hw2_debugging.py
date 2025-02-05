"""Homework 2 file for debugging and cleaning up"""

from rand import random_array

def merge_sort(array):
    """Used to merge sort the array"""
    if len(array) == 1:
        return array

    half = len(array)//2

    return recombine(merge_sort(array[:half]), merge_sort(array[half:]))

def recombine(left_arr, right_arr):
    """Used to recombine the array"""
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
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    while right_index < len(right_arr):
        merge_arr[left_index + right_index] = right_arr[right_index]
        right_index += 1
    while right_index < len(right_arr):
        merge_arr[left_index + right_index] = right_arr[right_index]
        right_index += 1

    while left_index < len(left_arr):
        merge_arr[left_index + right_index] = left_arr[left_index]
        left_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr

arr = random_array([None] * 20)

print(arr)

arr_out = merge_sort(arr)
arr_out = merge_sort(arr)

print(arr_out)
