# Iterators in Python

print("What is an Iterator?")
print("An iterator is an object that allows you to iterate over a sequence (such as a list, tuple, or string) and access each element one at a time.")

print("\nWhy Do We Need Iterators?")
print("Iterators are essential because they help us to:")
print("Iterate over large datasets without loading them into memory all at once")
print("Implement custom iteration logic")
print("Work with infinite sequences")

print("\nHow to Create an Iterator?")
print("You can create an iterator using the iter() function or by defining a class that implements the iterator protocol.")

print("\nIterator Protocol")
print("The iterator protocol consists of two methods:")
print("__iter__(): Returns the iterator object itself")
print("__next__(): Returns the next item in the sequence")

print("\n# Example 1: Creating an Iterator from a List\n")

my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
print(next(my_iter))  # Output: 4
print(next(my_iter))  # Output: 5

print("\n# Example 2: Implementing the Iterator Protocol\n")

class MyIterator:
    def __init__(self, data: int):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

my_iter = MyIterator([1, 2, 3, 4, 5])

for value in my_iter:
    print(value)

print("\n# Example 3: Using a Generator as an Iterator\n")

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

my_iter = my_generator()

for value in my_iter:
    print(value)

print("\n# Example 4: Using the itertools Module\n")

import itertools

my_list = [1, 2, 3, 4, 5]
my_iter = itertools.cycle(my_list)

for _ in range(10):
    print(next(my_iter))