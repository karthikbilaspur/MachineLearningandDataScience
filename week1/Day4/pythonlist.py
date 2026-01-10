# List :- 
#A list is a collection which is ordered and changeable. In Python, lists are written with square brackets.

# Creating a list
my_list = ["apple", "banana", "cherry"]
print(my_list)  # Output: ['apple', 'banana', 'cherry']
# Accessing elements
print(my_list[0])  # Output: apple

# Types of Lists :-
# 1. Empty List
empty_list = []
print(empty_list)  # Output: []

# 2. List of Integers
int_list = [1, 2, 3, 4, 5]
print(int_list)  # Output: [1, 2, 3, 4, 5]

# 3. List of Strings
str_list = ["hello", "world"]
print(str_list)  # Output: ['hello', 'world']

# 4. Mixed List
mixed_list = [1, "apple", 3.14, True]
print(mixed_list)  # Output: [1, 'apple', 3.14, True]

# 5. Nested List
nested_list = [[1, 2, 3], ["a", "b", " c"]]
print(nested_list)  # Output: [[1, 2, 3], ['a', 'b', ' c']]

# List Methods :-
# 1. append() - Adds an element at the end of the list
my_list.append("orange")
print(my_list)  # Output: ['apple', 'banana', 'cherry', 'orange']

# 2. insert() - Inserts an element at a specified position
my_list.insert(1, "kiwi")
print(my_list)  # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange']

# 3. remove() - Removes the first occurrence of a specified element
my_list.remove("banana")
print(my_list)  # Output: ['apple', 'kiwi', 'cherry', 'orange']

# 4. pop() - Removes and returns the element at the specified position (default is the last element)
last_item = my_list.pop()
print(last_item)  # Output: orange
print(my_list)  # Output: ['apple', 'kiwi', 'cherry']

# 5. sort() - Sorts the list in ascending order
num_list = [3, 1, 4, 2]
num_list.sort()
print(num_list)  # Output: [1, 2, 3, 4] 

# 6. reverse() - Reverses the order of the list
num_list.reverse()
print(num_list)  # Output: [4, 3, 2, 1]

# 7. count() - Returns the number of occurrences of a specified element
count_apple = my_list.count("apple")
print(count_apple)  # Output: 1
#8. extend() - Extends the list by appending elements from another list
another_list = ["grape", "melon"]
my_list.extend(another_list)
print(my_list)  # Output: ['apple', 'kiwi', 'cherry', 'grape', 'melon']

# 9. index() - Returns the index of the first occurrence of a specified element
index_kiwi = my_list.index("kiwi")
print(index_kiwi)  # Output: 1

# 10. clear() - Removes all elements from the list
my_list.clear()
print(my_list)  # Output: []

# List Comprehension :-
# A concise way to create lists
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Filtering with list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]

# Nested List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Conclusion :-
"""Lists are versatile and widely used in Python for storing collections of items.  
They support various methods for manipulation and can be created using list comprehensions for more concise code."""

