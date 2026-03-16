"""
Instructions:

Given two non-empty arrays of integers, write a function that determines whether the second array
is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but
that are in the same order as they appear in the array. For example, the numbers [1, 3, 4] form
a subsequence of the array [1, 2, 3, 4], and so do [2, 4].

You can assume that there will only be one subsequence.

Example:
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
Expected Output: True

Example 2:
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, 10, -1]
Expected Output: False (because -1 comes before 10 in the sequence, but after in the array)
"""


def isValidSubsequence(array, sequence):
    """
    Checks if 'sequence' is a valid subsequence of 'array'.
    A subsequence must maintain the original relative order.
    """
    if len(sequence) == 0:
        return False

    arr_idx = 0  
    seq_idx = 0  

    while arr_idx < len(array) and seq_idx < len(sequence):
        if array[arr_idx] == sequence[seq_idx]:
            seq_idx += 1
        arr_idx += 1

    return seq_idx == len(sequence)

if __name__ == '__main__':
    print(f"Test 1: {isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])}")  # True
    print(f"Test 2: {isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10, -1])}") # False