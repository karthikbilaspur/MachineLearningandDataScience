"""Sets in Python
A set in Python is an unordered collection of unique elements."""

# Types of Sets
# Standard Set: A set with elements of the same data type.

fruits = {"apple", "banana", "cherry"}

numbers = {1, 2, 3, 4, 5}
# Mixed Set: A set with elements of different data types.
mixed_set = {1, "hello", 3.14, True}

# Empty Set: A set with no elements.
empty_set = set()

#Frozen Set: An immutable set.

frozen_set = frozenset([1, 2, 3, 4, 5])


# Set with Tuple Elements: A set that contains tuples as elements.
set_with_tuples = {(1, 2), (3, 4), (5, 6)}

# Here's an example code snippet that demonstrates these types of sets:
# Standard Set
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Mixed Set
mixed_set = {1, "hello", 3.14, True}
print(mixed_set)  # Output: {1, 'hello', 3.14} (Note: True is not printed because it's equivalent to 1)

# Empty Set
empty_set = set()
print(empty_set)  # Output: set()

# Frozen Set
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)  # Output: frozenset({1, 2, 3, 4, 5})

# Set with Tuple Elements
set_with_tuples = {(1, 2), (3, 4), (5, 6)}
print(set_with_tuples)  # Output: {(1, 2), (3, 4), (5, 6)}
