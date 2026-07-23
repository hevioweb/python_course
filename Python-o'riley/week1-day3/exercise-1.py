#Exercise 1: Create a function to Calculate Factorials

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def print_factorial(n):
    result = factorial(n)
    print(f"The factorial of {n} is {result}")
    
print_factorial(5)  # Output: The factorial of 5 is 120 