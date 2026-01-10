# Memory Management in Python

print("What is Memory Management in Python?")
print("Memory management is the process of managing the memory used by a program, including allocating, deallocating, and optimizing memory usage. Python has an automatic memory management system, which means that the Python interpreter takes care of memory management for you.")

print("\nWhy Do We Need Memory Management?")
print("Memory management is essential because it helps to:")
print("Prevent memory leaks: Memory leaks occur when a program uses up all the available memory, causing the program to crash or become slow.")
print("Improve performance: Efficient memory management can improve the performance of a program by reducing the time it takes to access and manipulate data.")
print("Reduce errors: Memory management helps to prevent errors caused by accessing memory that has already been deallocated.")

print("\nHow Does Python Manage Memory?")
print("Python uses a combination of techniques to manage memory, including:")
print("Reference Counting: Python uses a reference counting system to keep track of the number of references to an object. When the reference count reaches zero, the object is deallocated.")
print("Garbage Collection: Python has a garbage collector that periodically cleans up unreachable objects and frees up memory.")
print("Memory Pools: Python uses memory pools to manage memory allocation and deallocation for small objects.")

print("\nTypes of Memory in Python")
print("There are two types of memory in Python:")
print("Stack Memory: Stack memory is used to store local variables and function call frames.")
print("Heap Memory: Heap memory is used to store objects and data structures.")

print("\n# Example 1: Reference Counting\n")

import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # Output: 2
y = x
print(sys.getrefcount(x))  # Output: 3
del y
print(sys.getrefcount(x))  # Output: 2

print("\n# Example 2: Garbage Collection\n")

import gc

class Test:
    def __init__(self):
        self.data = [1, 2, 3]

    def __del__(self):
        print("Object is being garbage collected")

obj = Test()
del obj
gc.collect()

print("\n# Example 3: Memory Pools\n")


x = [1, 2, 3]
print(sys.getsizeof(x))  # Output: 56 (or similar)
y = [1, 2, 3]
print(sys.getsizeof(y))  # Output: 56 (or similar)