# What are  comprehensions in python ? 
print("Comprehensions in Python are a concise way to create lists, sets, or dictionaries using a single line of code. They provide a syntactic shortcut for generating these collections by applying an expression to each item in an iterable (like a list or range) and optionally filtering items with a condition.")

#What are the types of comprehensions in python ?
print("There are three main types of comprehensions in Python: List Comprehensions, Set Comprehensions, and Dictionary Comprehensions.")
print("1. List Comprehensions: Used to create lists.")
print("2. Set Comprehensions: Used to create sets.")
print("3. Dictionary Comprehensions: Used to create dictionaries.")

# Give example of each type of comprehension in python ?
# Example of List Comprehension
squares = [x**2 for x in range(10)]
print("List Comprehension Example:", squares)
# Example of Set Comprehension
unique_squares = {x**2 for x in range(10)}
print("Set Comprehension Example:", unique_squares)
# Example of Dictionary Comprehension
square_dict = {x: x**2 for x in range(10)}
print("Dictionary Comprehension Example:", square_dict)

# What is the syntax of each type of comprehension in python ?
print("The syntax for each type of comprehension in Python is as follows:")
print("1. List Comprehension: [expression for item in iterable if condition]")
print("2. Set Comprehension: {expression for item in iterable if condition}")
print("3. Dictionary Comprehension: {key_expression: value_expression for item in iterable if condition}")

# How comprehensions are different from loops in python ?
print("Comprehensions are different from loops in Python in that they provide a more concise and readable way to create collections. While loops require multiple lines of code to initialize an empty collection, iterate over items, apply expressions, and append results, comprehensions allow you to achieve the same result in a single line. This can lead to cleaner and more efficient code. However, for complex operations or when readability is compromised, traditional loops may still be preferred.")

# When to use comprehensions in python ?
print("Comprehensions should be used in Python when you need to create a new collection (list, set, or dictionary) from an existing iterable in a concise and readable manner. They are particularly useful when the transformation or filtering logic is simple and can be expressed clearly in a single line. However, if the logic is complex or involves multiple steps, it may be better to use traditional loops for the sake of clarity and maintainability.")

# Can comprehensions be nested in python ? If yes, give example.
print("Yes, comprehensions can be nested in Python. This means you can have a comprehension inside another comprehension.")

# Example of Nested List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Nested List Comprehension Example (Flattening a matrix):", flattened)
# Example of Nested Dictionary Comprehension
nested_dict = {'a': [1, 2], 'b': [3, 4]}
squared_dict = {key: [x**2 for x in value] for key, value in nested_dict.items()}
print("Nested Dictionary Comprehension Example (Squaring values):", squared_dict)

# What are the advantages and disadvantages of comprehensions in python ?
print("Advantages of Comprehensions in Python:")
print("1. Conciseness: Comprehensions allow you to create collections in a single line of code, making it more concise.")
print("2. Readability: For simple transformations, comprehensions can be more readable than traditional loops.")
print("3. Performance: Comprehensions can be faster than equivalent loops due to optimizations in their implementation.")

print("Disadvantages of Comprehensions in Python:")
print("1. Complexity: For complex operations, comprehensions can become hard to read and understand.")
print("2. Debugging Difficulty: It can be more challenging to debug comprehensions compared to traditional loops.")
print("3. Limited Functionality: Comprehensions are best suited for simple transformations and may not be ideal for more complex logic that requires multiple steps.")

#Give real time use case of comprehensions in python ?
print("A real-time use case of comprehensions in Python is when processing data from a CSV file. For example, you might want to read a CSV file containing user information and create a list of usernames for users who are active.")
import csv
# Sample CSV data
csv_data = """username,active
user1,True
user2,False
user3,True
user4,True
"""
# Writing sample data to a CSV file
with open('users.csv', 'w') as file:
    file.write(csv_data)
# Reading the CSV file and using a list comprehension to extract active usernames
with open('users.csv', 'r') as file:
    reader = csv.DictReader(file)
    active_usernames = [row['username'] for row in reader if row['active'] == 'True']
print("Active Usernames from CSV:", active_usernames)

