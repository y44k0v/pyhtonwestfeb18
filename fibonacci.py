"""
Calculates the nth number in the Fibonacci sequence.
Example:
calculate_fibonacci(0) -> 0
calculate_fibonacci(1) -> 1
calculate_fibonacci(5) -> 5
"""
# Student must write their code here.
# For now, let's provide a placeholder that will fail the test.

def calculate_fibonacci(n: int) -> int:
    """Function takes an integer and returns the fibonacci number in
    the order specified by the said integer

    Args:
        n (int): integer that asks for nth Fibonacci number

    Returns:
        int: Returns the nth Fibonacci number
    """
    if n < 0:
        raise ValueError("the integer must be greater than or equal to 0")
    first = 0
    second = 1
    i = 0
    while i < n:
        copy = first
        first = second
        second = copy + second
        i += 1
    return first