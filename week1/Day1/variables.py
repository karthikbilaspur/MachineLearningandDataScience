# Python Variables #
"""Definition:
A variable is a named storage location that holds a value. In Python, variables are used to store and manipulate data.
Declaring Variables
In Python, you don't need to declare variables before using them. You can simply assign a value to a variable using the assignment operator (=).
Example:
Python """

# declaring variables
x = 5  # integer variable
y = 3.14  # float variable
name = "John"  # string variable
is_admin = True  # boolean variable

"""Variable Naming Rules
Variable names must start with a letter (a-z or A-Z) or an underscore (_).
Variable names can contain letters, numbers, and underscores.
Variable names cannot contain spaces or special characters.
Variable names are case-sensitive.
Example:"""

# valid variable names
x = 5
y_123 = 10
_name = "John"

"""# invalid variable names
1x = 5  # starts with a number
x! = 10  # contains a special character
x y = 15  # contains a space
Assigning Values to Variables
You can assign values to variables using the assignment operator (=)."""

x = 5
y = x  # assigns the value of x to y
print(y)  # prints 5

"""Multiple Assignments
You can assign multiple values to multiple variables in a single statement."""
x, y, z = 1, 2, 3
print(x, y, z)  # prints 1 2 3

"""Variable Types
Python variables can hold different data types, such as:
Integers (int): whole numbers, e.g., 1, 2, 3
Floats (float): decimal numbers, e.g., 3.14, -0.5
Strings (str): text, e.g., "hello", 'hello'
Boolean (bool): true or false values
Lists (list): ordered collections of values, e.g., [1, 2, 3]
Tuples (tuple): ordered, immutable collections of values, e.g., (1, 2, 3)
Dictionaries (dict): unordered collections of key-value pairs, e.g., {"name": "John", "age": 30}"""