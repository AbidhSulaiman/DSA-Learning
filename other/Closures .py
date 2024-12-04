"""

Closures in Python
********************
Using Functions within Functions to Retain State

A closure is a feature in Python where a nested function remembers and retains the state of variables in its enclosing scope,
even after the enclosing function has finished executing. Closures are powerful for creating function factories, encapsulating logic,
and maintaining state without using global variables or classes.

Key Concepts of Closures:
    1) A function defined inside another function(Nested Function).
    2) The outer function whose variables are accessible to the inner function.
    3) Even after the outer function has returned, the nested function remembers the values of variables in the outer scope(State retention).
    

"""
# Maintaining State

def counter():
    count = 0
    def increment():
        nonlocal count
        count +=1
        return count
    return increment
counting = counter()

# Function Factory

def main(n):
    def sub(m):
        return m*n
    return sub

double = main(2)
triple = main(3)
four = main(4)

# print(double(5))
# print(triple(5))
# print(four(5))


# encapsulation

def secure_data(password):
    def access_data(input_password):
        if password == input_password:
            print("Access Granted")
        else:
            print("Access Denied")    
    return access_data

password = secure_data('112')

password('1234')
password('112')