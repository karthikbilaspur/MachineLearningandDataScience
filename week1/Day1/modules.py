"""Modules in Python
A module is a file containing Python definitions and statements. Modules are used to organize related functions, classes, and variables in a single unit, making it easier to reuse code and reduce namespace pollution."""

"""Creating a Module
Let's create a simple module called math_utils.py:"""
# math_utils.py

from ast import Module
from doctest import Example


def add(a: int, b: int) -> int:
    """Return the sum of a and b"""
    return a + b

def multiply(a: int, b: int) -> int:
    """Return the product of a and b"""
    return a * b

"""Importing a Module
To use the math_utils module, we need to import it:
Python"""

# main.py
#import math_utils # Import the entire module

result = math_utils.add(2, 3)
print(result)  # Output: 5

#Importing Specific Functions # 
#We can also import specific functions from the module:#

# main.py
#from math_utils import add, multiply:#

result = add(2, 3)
print(result)  
# Output: 5

result = multiply(2, 3)
print(result) 
 # Output: 6

"""Using the as Keyword
We can use the as keyword to give the module or function a shorter alias:"""

# main.py
import math_utils as mu

result = mu.add(2, 3)
print(result) 
# Output: 5

"""The __name__ Variable
When a module is run directly (not imported), the __name__ variable is set to "__main__". We can use this to write code that should only run when the module is executed directly:"""
# math_utils.py
def add(a: int, b: int) -> int:
    """Return the sum of a and b"""
    return a + b

if __name__ == "__main__":
    print("Running math_utils module directly")
    result = add(2, 3)
    print(result)  
    # Output: 5
"""Example Use Case
Let's create a calculator.py module that imports and uses the math_utils module:"""


# calculator.py
import math_utils

def calculate_expression(a: int, b: int, op: str) -> int:
    if op == "add":
        return math_utils.add(a, b)
    elif op == "multiply":
        return math_utils.multiply(a, b)
    else:
        raise ValueError("Invalid operation")

if __name__ == "__main__":
    result = calculate_expression(2, 3, "add")
    print(result)  # Output: 5
"""
Commit message:
Code
Add math_utils module with add and multiply functions

* Create math_utils.py module with add and multiply functions
* Update main.py to import and use math_utils module
* Add calculator.py module that imports and uses math_utils module """