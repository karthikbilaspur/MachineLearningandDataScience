# Dictionaries in Python
# A dictionary in Python is a collection of key-value pairs.
# Each key is unique and is used to access the corresponding value.

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values
print(my_dict["name"])  # Output: Alice

# Adding a new key-value pair
my_dict["job"] = "Engineer" 
print(my_dict)

# Updating an existing value
my_dict["age"] = 26 
print(my_dict)

# Removing a key-value pair
del my_dict["city"] 
print(my_dict)

# Looping through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 26
# job: Engineer

# Checking if a key exists
if "name" in my_dict:
    print("Name is present in the dictionary.")
# Output: Name is present in the dictionary.

# Getting the number of key-value pairs
print(len(my_dict))  # Output: 3

# Clearing all items in the dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# Types of Dictionaries
# 1. Standard Dictionary
standard_dict = {
    "fruit": "apple",
    "color": "red",
    "quantity": 10
}

# 2. Nested Dictionary
nested_dict = {
    "person1": {
        "name": "Bob",
        "age": 30
    },
    "person2": {
        "name": "Charlie",
        "age": 35
    }
}

# 3. Dictionary with Different Data Types
mixed_dict = {
    "name": "Diana",
    "age": 28,
    "is_student": False,
    "grades": [85, 90, 88]
}

# 4. Empty Dictionary
empty_dict = {}

# 5. Dictionary with Tuple Keys
tuple_key_dict = {
    (1, 2): "point A",
    (3, 4): "point B"
}

