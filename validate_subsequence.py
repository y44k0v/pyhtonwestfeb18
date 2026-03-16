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
    if len(sequence) == 0:
        return False
    
    array_position = 0
    sequence_position = 0
    
    while array_position < len(array) and sequence_position < len(sequence):
        
        if array[array_position] == sequence[sequence_position]:
            sequence_position = sequence_position + 1
            
        array_position = array_position + 1
        
    if sequence_position == len(sequence):
        
        
        return True
    else:
        return False