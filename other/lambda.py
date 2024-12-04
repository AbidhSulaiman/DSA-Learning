"""
Lambda Functions

Lambda functions are anonymous, concise functions in Python often used for short operations.
They are especially powerful when paired with functions like map(), filter(), and reduce().

Basic Syntax :

    lambda argumets: expression
    
    Eg:
        Squares = lambda x: X**2
        Squares(5) // return 25
        
Using map() with Lambda Functions
----------------------------------

The map() function applies a function to each item in an iterable (like a list or tuple) and returns a map object (an iterator).
Basic Example:
    nums = [1, 2, 3, 4]
    squared = map(lambda x: x ** 2, nums)
    print(list(squared))  # Output: [1, 4, 9, 16]
    
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    summed = map(lambda x, y: x + y, nums1, nums2)
    print(list(summed))  # Output: [5, 7, 9]

Using filter() with Lambda Functions
-------------------------------------

The filter() function filters items in an iterable based on a condition defined in the function.

Example:
    nums = [1, 2, 3, 4, 5]
    even = filter(lambda x: x % 2 == 0, nums)
    print(list(even))  # Output: [2, 4]
    
Example 2:
    emails = ["abc@example.com", "invalid@", "hello@gmail.com"]
    valid_emails = filter(lambda e: "@" in e and "." in e, emails)
    print(list(valid_emails))  # Output: ['abc@example.com', 'hello@gmail.com']

Using reduce() with Lambda Functions
---------------------------------------
The reduce() function, part of the functools module, reduces a sequence to a single value by applying a function cumulatively.

Example1:
    from functools import reduce

    nums = [1, 2, 3, 4]
    total = reduce(lambda x, y: x + y, nums)
    print(total)  # Output: 10

Example1:

    words = ["Python", "is", "fun"]
    sentence = reduce(lambda x, y: x + " " + y, words)
    print(sentence)  # Output: 'Python is fun'
    
When to Use Lambda Functions
--------------------------------
    Quick one-off functions: If the logic is simple and doesn't need to be reused.
    Combining with functional tools: map(), filter(), and reduce() are excellent candidates.
    Readable code: For concise and clear operations.
    
Limitations of Lambda Functions
---------------------------------
    No multi-line operations: Lambdas are restricted to a single expression.
    Readability: Overusing lambdas can make code harder to read and debug.
    No return keyword: The result of the expression is implicitly returned.


"""

# Sum of Squares of Even Numbers from a list

from functools import reduce

nums = [1, 2, 3, 4, 5]
even_squared_sum = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums))
)
# print(even_squared_sum)  # Output: 20


# Product of Odd Numbers

product_of_numbers = reduce(lambda x,y: x*y, filter(lambda x: x % 2 !=0, nums))
# print(product_of_numbers)

# Longest Word Length

list_string = ['abidh','sulaiman','abs']
longest_string_length = reduce(lambda x,y: x if x>y else y, map(lambda x: len(x), list_string))
# print(longest_string_length)

# Sum of Cubes of Numbers Divisible by 3

numbers = [3,5,6,8,9]
dvisible_by_3 = reduce(lambda x,y : x+y, map(lambda x: x**3,filter(lambda x: x%3 == 0, numbers)))

# Count of Palindromic Words

palindrom_words = ['aba', 'bca', 'cbc']
palindrom_count = len(list(filter(lambda x: x == x[::-1], palindrom_words)))
# print(palindrom_count)

#Find the Maximum of Squares of Negative Numbers
negative_numbers = [1,2,-3,-5,8]

max_value = reduce(lambda x,y: x if x>y else y, map(lambda x: x**2, filter(lambda x: x<0, negative_numbers)))

# print(max_value)

#------------------------------------------------------------------

# Filter and Reverse Words Longer than 4 Letters

string_list = ['abidh', 'ab', 'sulaiman', 'dc']

reversed_words = map(lambda x:x[::-1], filter(lambda x: len(x)>4, string_list))

# print(list(reversed_words))

# Sum of Digits of All Numbers

nums = [11,22]
digits_sum = map(lambda x: sum(map(int, str(x))), nums)

total_sum = reduce(lambda x, y: x + y, digits_sum)

print(total_sum)






