"""Input and Output in Python 
Definition:
Input refers to the data provided to a program, while output refers to the data produced by a program. Python provides several ways to handle input and output operations.
Input in Python
The input() function is used to take input from the user.
The input is taken as a string by default.
Output in Python
The print() function is used to produce output.
The output can be a string, integer, float, or any other data type."""

#Example 1: Simple Input and Output # 

# Take input from the user
name = input("Enter your name: ")

# Print the input
print("Hello, " + name + "!")


"""Enter your name: John
Hello, John!"""

#Example 2: Input and Output with Data Types # 
# Take input from the user
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))

# Print the input
print("You are", age, "years old and", height, "meters tall.")


"""Enter your age: 25
Enter your age: 25
Enter your height (in meters): 1.75
You are 25 years old and 1.75 meters tall. """