# Recursive Fibonacci function
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Iterative Fibonacci function
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage to call both methods separately:
n = 10

# Call the recursive Fibonacci function
recursive_result = fibonacci_recursive(n)
print(f"Recursive Fibonacci of {n} is: {recursive_result}")

# Call the iterative Fibonacci function
iterative_result = fibonacci_iterative(n)
print(f"Iterative Fibonacci of {n} is: {iterative_result}")
