print("What is File Handling?")
print("File handling in Python refers to the process of working with files, including reading from and writing to files, as well as performing other operations such as creating, deleting, and modifying files.")
print("Python provides several built-in functions and methods for file handling, including open(), read(), write(), close(), and others, which allow you to interact with files and perform various operations on them.")

print("\n Example 1: Reading a File\n")

# Open the file in read mode
file = open("exp.txt", "r")

# Read the contents of the file
contents = file.read()

# Print the contents
print(contents)

# Close the file
file.close()

print("\n Example 2: Writing to a File\n")

# Open the file in write mode
file = open("exp.txt", "w")

# Write to the file
file.write("Hello, World!")

# Close the file
file.close()

print("\n Example 3: Appending to a File\n")

# Open the file in append mode
file = open("exp.txt", "a")

# Append to the file
file.write(" This is a new line.")

# Close the file
file.close()

print("\n Example 4: Reading a File Line by Line\n")

# Open the file in read mode
file = open("exp.txt", "r")

# Read the file line by line
for line in file:
    print(line)

# Close the file
file.close()

print("\n Example 5: Using a with Statement\n")

# Open the file in read mode using a with statement
with open("exp.txt", "r") as file:
    # Read the contents of the file
    contents = file.read()
    print(contents)

#  Note: The with statement automatically closes the file when you're done with it, so you don't need to call file.close() explicitly.

print("\nFile Modes are as follows:")
print("r: Read mode (default)")
print("w: Write mode")
print("a: Append mode")
print("x: Create mode (exclusive creation)")
print("b: Binary mode")
print("t: Text mode (default)")
print("+ : Update mode (read and write)")