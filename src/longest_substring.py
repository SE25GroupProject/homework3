"""
Module for finding the length of the longest substring without repeating characters.
"""

def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest substring without repeating characters.
    """
    chars = set()
    l, r = 0, 0
    record = 0
    while r < len(s):
        prev_len = len(chars)
        chars.add(s[r])
        if len(chars) == prev_len:
            while s[l] != s[r]:
                chars.remove(s[l])
                l += 1
            l += 1
        r += 1
        if len(chars) > record:
            record = len(chars)
    return record
