#Lambda:- Any function without ts name is called lambda function.

add = lambda x, y: x + y
result = add(3, 5)
print(result)  

# Output: 8

# Lambda function to calculate the square of a number
square = lambda x: x ** 2
print(square(4))  # Output: 16

# Lambda function to find the maximum of two numbers
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))  # Output: 20

# Lambda function to filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6]

# Lambda function to sort a list of tuples based on the second element

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# Lambda function to calculate the factorial of a number using recursion

factorial = (lambda f: lambda x: f(f, x))(lambda f, x: 1 if x == 0 else x * f(f, x - 1))
print(factorial(5))  # Output: 120

# Lambda function to convert temperatures from Celsius to Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32
print(celsius_to_fahrenheit(25))  # Output: 77.0