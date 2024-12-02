"""
What is Recursion?
Recursion is a programming concept where a function calls itself to solve a problem. This technique is particularly useful for problems
that can be broken down into smaller, similar subproblems.In Python, recursion is implemented using function calls, 
with each recursive call solving a smaller instance of the original problem.

How Does Recursion Work?
A recursive function works in two main stages:

Base Case:

    This is the condition under which the recursion stops. Without a base case, the function would call itself indefinitely,
    leading to a RecursionError in Python.
    
Recursive Case:

    * This is the part where the function calls itself to process a smaller problem.
Each recursive call creates a new instance of the function, with its own execution context.
Once the base case is met, the call stack unwinds, and the function returns results step by step.

Basic Syntax:

    def recursive_function(parameters):
        if base_condition:  # Base case
            return result
        else:
            # Recursive case
            return recursive_function(modified_parameters)

"""

# Examples
# 1) factorial of a number

def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Example usage
print(factorial(5))  # Output: 120

# 2) Fibonacci Sequence

def fibonacci(n):
    if n == 0:  # Base case 1
        return 0
    elif n == 1:  # Base case 2
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Example usage
print(fibonacci(6))  # Output: 8

"""

Visualizing Recursion with a Call Stack
Consider the factorial example for n=3:

1) factorial(3) calls factorial(2)
2) factorial(2) calls factorial(1)
3) factorial(1) calls factorial(0) (Base case)
4) The base case returns 1, and the stack unwinds:
    factorial(1) returns 1 * 1 = 1
    factorial(2) returns 2 * 1 = 2
    factorial(3) returns 3 * 2 = 6
Each recursive call pauses execution until the function it called returns a value.

"""