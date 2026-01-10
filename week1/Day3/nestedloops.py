"""Nested Loops
A Nested Loop is a loop inside another loop. The inner loop will execute its entire cycle for each iteration of the outer loop.
Types of Nested Loops:
Nested For Loops: Used to iterate over two or more sequences.
Nested While Loops: Used to execute a block of code repeatedly as long as a certain condition is true, with an inner loop that executes repeatedly for each iteration of the outer loop.
"""

# Nested For Loops
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i: {i}, j: {j}")

# Nested While Loops
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i: {i}, j: {j}")
        j += 1
    i += 1

# Nested Loop with User Input
while True:
    outer_input = input("Enter 'exit' to quit outer loop or any key to continue: ")
    if outer_input.lower() == 'exit':
        print("Exiting the outer loop.")
        break
    else:
        print("Inside outer loop.")
        while True:
            inner_input = input("Enter 'back' to go back to outer loop or any key to continue: ")
            if inner_input.lower() == 'back':
                print("Going back to outer loop.")
                break
            else:
                print("Inside inner loop.")

# Nested Loop with Break and Continue
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue  # Skip when j is 2
        if i == 3 and j == 3:
            break  # Break inner loop when i is 3 and j is 3
        print(f"i: {i}, j: {j}")

# Nested Loop with Else
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")
    else:
        print(f"Completed inner loop for i = {i}")

# Nested Loop with User Input and Break
while True:
    outer_input = input("Enter 'exit' to quit outer loop or any key to continue: ")
    if outer_input.lower() == 'exit':
        print("Exiting the outer loop.")
        break
    else:
        print("Inside outer loop.")
        while True:
            inner_input = input("Enter 'back' to go back to outer loop or 'exit' to quit: ")
            if inner_input.lower() == 'back':
                print("Going back to outer loop.")
                break
            elif inner_input.lower() == 'exit':
                print("Exiting both loops.")
                exit()
            else:
                print("Inside inner loop.")