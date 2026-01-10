"""For Loop
A For Loop is a control structure in programming that allows you to execute a block of code repeatedly for a specified number of times.
Types of For Loops:
Traditional For Loop: Used to iterate over a sequence (like an array or list) using an index.
Enhanced For Loop (or For-Each Loop): Used to iterate over a sequence (like an array or list) directly, without using an index.
Range-Based For Loop: Used to iterate over a range of values.
"""

for i in range(5):
    print(i, end=" ")

#Sequence-Based For Loop

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Range-Based For Loop with start, stop, and step
for i in range(1, 6, 2):
    print(i, end=" ")

# Enumerate For Loop (with index and value)
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Dictionary For Loop (with key and value)

person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(f"{key}: {value}")

# Nested For Loop
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i: {i}, j: {j}")

# For Loop with Break and Continue
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
for i in range(5):
    if i == 3:
        continue
    print(i, end=" ")
# For Loop with Else
for i in range(5):
    print(i, end=" ")
else:
    print("Loop finished")

# For Loop with User Input
while True:
    user_input = input("Enter 'exit' to quit: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {user_input}")

# For Loop with List Comprehension
squares = [x**2 for x in range(5)]
print(squares)
