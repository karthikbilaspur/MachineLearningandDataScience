# Definition
'''A string is a sequence of characters enclosed in quotes.'''


s = "Hello, World!"

# Quotes

# Single quotes: 
s = 'Hello, World!'

# Double quotes: 
s = "Hello, World!"

# Triple quotes:

s = '''Hello, World!'''

s = """Hello,
World!"""

# Indexing

# Positive indices:   s[0] gives 'H'

# Negative indices:   s[-1] gives '!\n'

s = "Hello"
print(s[0])   # H
print(s[-1])  # o

# Slicing
s = "Hello"
print(s[1:3])  # el

# Immutability

s = "Hello"
# s[0] = 'h'  # TypeError
s = "h" + s[1:]  # create a new string

# Operations

# Concatenation: s1 + s2

s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # Hello World

# Repetition: s * n
s = "Hello"
print(s * 2)  

# HelloHello

# Membership testing: substr in s

s = "Hello"
print("He" in s)  # True

# Methods  len(): len(s)
s = "Hello"
print(len(s))  # 5

# upper(): s.upper()
s = "hello"
print(s.upper())  # HELLO
# lower(): s.lower()

s = "HELLO"
print(s.lower())  # hello
# strip(): s.strip()

s = "  Hello  "
print(s.strip())  # Hello

# replace():  s.replace(old: str, new: str)

s = "Hello"

print(s.replace("H", "h"))  # hello  format(): s.format()

name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# My name is John and I am 30 years old.

# Formatting f-strings: f"{var}"

name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
# My name is John and I am 30 years old.

# format() method: "{}".format(var)
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# My name is John and I am 30 years old