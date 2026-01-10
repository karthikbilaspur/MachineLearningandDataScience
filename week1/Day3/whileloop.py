"""While Loop
A While Loop is a control structure in programming that allows you to execute a block of code repeatedly as long as a certain condition is true.
Types of While Loops:
Simple While Loop: Used to execute a block of code repeatedly as long as a certain condition is true.
While Loop with Else: Used to execute a block of code repeatedly as long as a certain condition is true, and execute an else block when the condition becomes false.
"""
#Simple While Loop
i = 0
while i < 5:
    print(i, end=" ")
    i += 1

# While Loop with Else
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
else:
    print("Loop finished")

# Infinite While Loop
i = 0
while True:
    print(i, end=" ")
    i += 1
    if i == 5:
        break

# While Loop with Break and Continue
i = 0
while i < 5:
    if i == 3:
        break
    print(i, end=" ")
    i += 1


i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i, end=" ")

# Nested While Loop
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i: {i}, j: {j}")
        j += 1
    i += 1

# While Loop with User Input
while True:
    user_input = input("Enter 'exit' to quit: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {user_input}")

# While Loop with a Condition Based on a List
numbers = [1, 2, 3, 4, 5]
index = 0
while index < len(numbers):
    print(numbers[index], end=" ")
    index += 1
    