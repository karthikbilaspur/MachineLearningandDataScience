# Program to demonstrate loops and statements in Python

# Section 1: For Loop
print("Section 1: For Loop")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Section 2: While Loop
print("\nSection 2: While Loop")
i = 0
while i < 5:
    print(i)
    i += 1

# Section 3: Loop Control Statements
print("\nSection 3: Loop Control Statements")
print("Break Statement:")
for i in range(5):
    if i == 3:
        break
    print(i)

print("\nContinue Statement:")
for i in range(5):
    if i == 3:
        continue
    print(i)

# Section 4: Nested Loops
print("\nSection 4: Nested Loops")
fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'green', 'yellow']

for fruit in fruits:
    for color in colors:
        print(f"{fruit} is {color}")

# Section 5: If-Else Statement
print("\nSection 5: If-Else Statement")
x = 5
if x > 10:
    print("x is big")
else:
    print("x is small")

# Section 6: Pass Statement
print("\nSection 6: Pass Statement")
for i in range(5):
    if i == 3:
        pass
    print(i)

# Section 7: Return Statement
print("\nSection 7: Return Statement")
def add(a: int, b: int) -> int:
    return a + b

result = add(2, 3)
print("Result:", result)