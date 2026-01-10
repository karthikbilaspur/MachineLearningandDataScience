"""Python Functions
Python functions are reusable blocks of code that perform a specific task. They can take arguments, return values, and be called multiple times from different parts of the program.
"""

# Key Points:
"""Defined using the def keyword
Can take arguments (parameters) and return values
Can be called multiple times from different parts of the program
Support various types of arguments: default, keyword, positional, and arbitrary
Can be nested inside other functions
Can be anonymous (lambda functions)
Use the return statement to send a value back to the caller
Pass by object reference (mutable objects can be modified, immutable objects cannot)
Types of Function Arguments:
Default Arguments: assume a default value if not provided
Keyword Arguments: values passed by explicitly specifying the parameter name
Positional Arguments: values assigned to parameters based on their order
Arbitrary Arguments: variable number of arguments using *args and **kwargs
Function Examples:
Simple function: def greet(): print("Hello")
Function with arguments: def add(x, y): return x + y
Function with default argument: def greet(name = "World"): print("Hello, " + name)
Lambda function: cube = lambda x: x ** 3
"""
# Simple Function
def greet():
    print("Hello")
greet()

# Function with Arguments
def add(x: int, y: int) -> int:
    return x + y
result = add(3, 5)
print(f"Sum: {result}")

# Function with Default Argument
def greet(name: str = "World"):
    print(f"Hello, {name}!")
greet()
greet("Alice")

# Lambda Function
cube = lambda x: x ** 3
print(f"Cube of 3: {cube(3)}")

# Function with Arbitrary Arguments
def arbitrary_args(*args: any, **kwargs: any):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
arbitrary_args(1, 2, 3, name="Alice", age=30)

# Nested Function
def outer_function(text: str):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from nested function!")

