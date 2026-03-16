"""
Instructions:

Write a function that takes in a non-empty array of integers that are sorted in ascending order
and returns a new array of the same length with the squares of the original integers also
sorted in ascending order.

Example:
array = [1, 2, 3, 5, 6, 8, 9]
Expected Output: [1, 4, 9, 25, 36, 64, 81]

Example with negative numbers:
array = [-2, -1, 0, 1, 2]
Expected Output: [0, 1, 1, 4, 4]
"""

def sortedSquaredArray(array):
    length = len(array)
    result_array = [0] * length
    
    start_of_array = 0
    end_of_array = length - 1
    
    position_to_fill = length - 1
    
    while position_to_fill >= 0:
      
        start_val = array[start_of_array]
        end_val = array[end_of_array]
        if abs(start_val) > abs(end_val):
            result_array[position_to_fill] = start_val * start_val
            start_of_array = start_of_array + 1
        else:
            result_array[position_to_fill] = end_val * end_val
            end_of_array = end_of_array - 1
            
        position_to_fill = position_to_fill - 1
        
    return result_array
                          