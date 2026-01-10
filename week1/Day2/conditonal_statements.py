
# conditional_statements.py

# If Conditional Statement
print("If Conditional Statement:")
age = 20
if age >= 18:
    print("Eligible to vote.")

# Short Hand if
print("\nShort Hand if:")
age = 19
if age > 18: print("Eligible to Vote.")

# If else Conditional Statement
print("\nIf else Conditional Statement:")
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

# Short Hand if-else
print("\nShort Hand if-else:")
marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")

# elif Statement
print("\nelif Statement:")
age = 25
if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

# Nested if..else Conditional Statement
print("\nNested if..else Conditional Statement:")
age = 70
is_member = True
if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

# Ternary Conditional Statement
print("\nTernary Conditional Statement:")
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

# Match-Case Statement
print("\nMatch-Case Statement:")
number = 2
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")