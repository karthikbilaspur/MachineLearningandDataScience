
# Regular Expressions in Python

print("What is Regular Expression?")
print("A regular expression, commonly referred to as regex, is a sequence of characters that forms a search pattern. It can be used to check if a string contains the specified search pattern.")

print("\nWhy Do We Need Regular Expressions?")
print("Regular expressions are essential because they help us to:")
print("Search for patterns in strings")
print("Validate input data")
print("Extract data from strings")
print("Replace data in strings")

print("\nHow to Use Regular Expressions in Python?")
print("Python has a built-in module called 're' that provides support for regular expressions.")

print("\nCommon Regular Expression Patterns")
print("Some common regular expression patterns are:")
print(". : Matches any single character")
print("^ : Matches the start of a string")
print("$ : Matches the end of a string")
print("* : Matches zero or more occurrences of the preceding character")
print("+ : Matches one or more occurrences of the preceding character")
print("? : Matches zero or one occurrence of the preceding character")
print("{n} : Matches exactly n occurrences of the preceding character")
print("[abc] : Matches any character in the set")
print("[^abc] : Matches any character not in the set")

print("\n# Example 1: Searching for a Pattern\n")

import re

text = "Hello, my phone number is 123-456-7890"
pattern = r'\d{3}-\d{3}-\d{4}'
match = re.search(pattern, text)
if match:
    print("Phone number found:", match.group())
else:
    print("No phone number found")

print("\n# Example 2: Validating Input Data\n")


email = "test@example.com"
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
if re.match(pattern, email):
    print("Email is valid")
else:
    print("Email is not valid")

print("\n# Example 3: Extracting Data from a String\n")


text = "My name is John Doe and I am 30 years old"
pattern = r'\d+'
match = re.search(pattern, text)
if match:
    print("Age:", match.group())
else:
    print("No age found")

print("\n# Example 4: Replacing Data in a String\n")


text = "Hello, my name is John Doe"
pattern = r'John'
replacement = "Jane"
new_text = re.sub(pattern, replacement, text)
print(new_text)

text = "Visit https://www.google.com for more information. You can also check https://www.stackoverflow.com for answers."
pattern = r'https?://\S+'
urls = re.findall(pattern, text)
print("URLs:", urls)

password = "P@ssw0rd"
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
if re.match(pattern, password):
    print("Password is strong")
else:
    print("Password is not strong")

text = "My birthday is 12/25/1995 and my anniversary is 06/15/2010."
pattern = r'\d{1,2}/\d{1,2}/\d{4}'
dates = re.findall(pattern, text)
print("Dates:", dates)

text = "You can contact me at 123-456-7890 or 098-765-4321."
pattern = r'\d{3}-\d{3}-\d{4}'
replacement = "(XXX) XXX-XXXX"
new_text = re.sub(pattern, replacement, text)
print(new_text)
