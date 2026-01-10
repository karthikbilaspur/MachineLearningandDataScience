# data_types.py

# Numeric Data Types
print("Numeric Data Types:")
a = 5
print(type(a))  # int
b = 5.0
print(type(b))  # float
c = 2 + 4j
print(type(c))  # complex

# Sequence Data Types
print("\nSequence Data Types:")
s = 'Welcome to the India World'
print(s)
print(type(s))  # str
print(s[1])  # e
print(s[2])  # l
print(s[-1])  # d

# List Data Type
print("\nList Data Type:")
a = [1, 2, 3]
print(a)
b = ["India", "For", "India", 4, 5]
print(b)
print(b[0])  # India
print(b[-1])  # 5

# Tuple Data Type
print("\nTuple Data Type:")
tup1 = (1, 2, 3, 4, 5)
print(tup1)
print(tup1[0])  # 1
print(tup1[-1])  # 5

# Boolean Data Type
print("\nBoolean Data Type:")
print(type(True))  # bool
print(type(False))  # bool

# Set Data Type
print("\nSet Data Type:")
s1 = set("IndiaForIndia")
print(s1)
s2 = set(["India", "For", "India"])
print(s2)
for i in s2:
    print(i, end=" ")  # For India
print("India" in s2)  # True

# Dictionary Data Type
print("\nDictionary Data Type:")
d = {1: 'India', 2: 'For', 3: 'India'}
print(d)
print(d[1])  # India 
print(d.get(3))  # India 