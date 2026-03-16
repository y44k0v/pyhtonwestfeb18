"""
    Calculates the nth number in the Fibonacci sequence.
    Example:
    calculate_fibonacci(0) -> 0
    calculate_fibonacci(1) -> 1
    calculate_fibonacci(5) -> 5
"""
    # Student must write their code here.
    # For now, let's provide a placeholder that will fail the test.

def calculate_fibonacci(n):
        if n < 0: 
            raise ValueError("Nagative number")
        x = 0
        y = 1
        for _ in range(n):
            
            current_value = x
            x = y 
            y = current_value + y

        return x
