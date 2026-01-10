# Exception Handling in Python

print("What is Exception Handling?")
print("Exception handling is a mechanism in Python that allows you to handle and manage errors or exceptions that occur during the execution of your code. An exception is an event that occurs during the execution of a program, such as a division by zero or an attempt to access an index that is out of range.")

print("\nWhy Do We Need Exception Handling?")
print("Exception handling is essential because it helps you to:")
print("Handle unexpected errors and prevent your program from crashing")
print("Provide a way to recover from errors and continue executing the program")
print("Improve the overall reliability and robustness of your code")

print("\nTypes of Exceptions")
print("There are two types of exceptions in Python:")
print("Built-in Exceptions: These are exceptions that are built into Python, such as ZeroDivisionError, TypeError, and IndexError.")
print("User-Defined Exceptions: These are exceptions that you can define yourself using the class keyword.")

print("\nTry-Except Block")
print("The try-except block is used to handle exceptions in Python. The basic syntax is:")
print("try:")
print("    # Code that might raise an exception")
print("except ExceptionType:")
print("    # Code to handle the exception")

print("\n# Example 1: Handling a ZeroDivisionError\n")

try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("\n# Example 2: Handling a TypeError\n")

try:
    x = "hello" + 5
except TypeError:
    print("Cannot concatenate a string and an integer!")

print("\n# Example 3: Handling Multiple Exceptions\n")

try:
    x = 5 / 0
except (ZeroDivisionError, TypeError):
    print("An error occurred!")

print("\n# Example 4: Using the 'as' Keyword\n")

try:
    x = 5 / 0
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")

print("\n# Example 5: Using a Finally Block\n")

try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This code will always run!")

# Creating a user-defined exception
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance!")
    else:
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: {balance}")

print("\n# Example 6: User-Defined Exception\n")

try:
    withdraw(1000, 1500)
except InsufficientBalanceError as e:
    print(e)