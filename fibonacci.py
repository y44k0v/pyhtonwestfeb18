def calculate_fibonacci(n):
    """
    Calculates the nth number in the Fibonacci sequence.
    Example:
    calculate_fibonacci(0) -> 0
    calculate_fibonacci(1) -> 1
    calculate_fibonacci(5) -> 5
    """
    # TODO: Student must write their code here.
    # For now, let's provide a placeholder that will fail the test.


    if n < 0:
        return False
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    x = 0
    y = 1


    for _ in range(2, n + 1):
        x, y = y, x + y  

    return y 

if __name__ == "__main__":
    print(calculate_fibonacci(-2)) # False
    print(calculate_fibonacci(0))   # 0
    print(calculate_fibonacci(1))   # 1
    print(calculate_fibonacci(7))   # 13
    print(calculate_fibonacci(9))  # 34


    # return -1