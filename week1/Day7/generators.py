# Generators in Python

print("What is a Generator?")
print("A generator is a special type of function that can be used to generate a sequence of values instead of computing them all at once and returning them in a list, for example.")

print("\nWhy Do We Need Generators?")
print("Generators are essential because they help us to:")
print("Create iterators in a simple way")
print("Handle large datasets without loading them into memory all at once")
print("Implement cooperative multitasking")

print("\nHow to Create a Generator?")
print("You can create a generator using the yield keyword.")

print("\nGenerator Syntax")
print("The generator syntax is similar to the function syntax, but instead of using the return keyword, you use the yield keyword.")

print("\n# Example 1: Simple Generator\n")

def my_generator():
    yield 1
    yield 2
    yield 3

my_gen = my_generator()

print(next(my_gen))  # Output: 1
print(next(my_gen))  # Output: 2
print(next(my_gen))  # Output: 3

print("\n# Example 2: Generator with a Loop\n")

def my_generator(n):
    for i in range(n):
        yield i

my_gen = my_generator(5)

for value in my_gen:
    print(value)

print("\n# Example 3: Generator with a Condition\n")

def my_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

my_gen = my_generator(10)

for value in my_gen:
    print(value)

print("\n# Example 4: Generator Expression\n")

my_gen = (i for i in range(5))

for value in my_gen:
    print(value)

print("\n# Example 5: Using Generators with itertools Module\n")

import itertools

def my_generator():
    yield 1
    yield 2
    yield 3

my_gen = my_generator()
my_gen = itertools.chain(my_gen, my_gen)

for value in my_gen:
    print(value)