"""What is tuples in Python?
A tuple in Python is an ordered, immutable collection of items.
Tuples are similar to lists, but unlike lists, tuples cannot be modified after their creation (i.e., they are immutable). 
Tuples are defined by enclosing the items in parentheses ().
"""
# Creating a tuple



my_tuple = (1, 2, 3, "hello", True)
"""
# Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: hello
# Tuples are immutable, so you cannot add, remove, or change elements
# However, you can concatenate tuples to create a new tuple
new_tuple = my_tuple + (4, 5)
print(new_tuple)  # Output: (1, 2, 3, 'hello, True, 4, 5)
"""

# Looping through a tuple
for item in my_tuple:
    print(item)
# Output:
# 1
# 2
# 3

# Checking if an item exists
if "hello" in my_tuple:
    print("Found hello in the tuple.")
# Output: Found hello in the tuple.
# Getting the number of items
print(len(my_tuple))  # Output: 5

# Nested tuples
nested_tuple = (1, 2, (3, 4), (5, 6))
print(nested_tuple[2])  # Output: (3, 4)

# Output:
# 1
# 2
# 3
# 4
# True
# 5

my_tuple = ({"person1": {"name": "Eve", "age": 22}}, {(3, 4): "point B"})


# Types of Tuples
# 1. Standard Tuple
standard_tuple = (10, 20, 30, 40, 50)
# 2. Nested Tuple
nested_tuple = (1, 2, (3, 4), (5, 6))
# 3. Tuple with Different Data Types
mixed_tuple = (1, "hello", 3.14, True, [1, 2, 3])
# 4. Single Element Tuple
single_element_tuple = (42,)

# 5. Empty Tuple
empty_tuple = ()


# 6. Tuple with Tuple Elements
tuple_of_tuples = ((1, 2), (3, 4), (5, 6))
# 7. Immutable Tuple
immutable_tuple = (100, 200, 300)

