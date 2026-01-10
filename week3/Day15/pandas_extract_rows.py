#pandas_extract_rows_iloc.py
import pandas as pd
def display_extract_rows_iloc_info():
# Display information about extracting rows using Pandas .iloc[].
print("# Extracting Rows using Pandas .iloc[] #")
print("------------------------------------------")
print("The .iloc[] method is used to extract rows from a DataFrame based on their position.")
print("It is primarily integer position based (from 0 to length-1 of the axis).")
print()
print("Syntax:")
print("df.iloc[row_selection, column_selection]")
print()
print("Parameters:")
print("row_selection: An integer, a list of integers, or a slice of integers.")
print("column_selection: An integer, a list of integers, or a slice of integers.")
def example_extract_rows_iloc():
# Example usage of extracting rows using Pandas .iloc[].
# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
'Age': [28, 24, 35, 32],
'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data)
Code
print("\n# Example 1: Extract a single row #")
print(df.iloc[0])

print("\n# Example 2: Extract multiple rows #")
print(df.iloc[[0, 2]])

print("\n# Example 3: Extract a range of rows #")
print(df.iloc[0:2])

print("\n# Example 4: Extract rows with a step #")
print(df.iloc[::2])

print("\n# Example 5: Extract rows in reverse order #")
print(df.iloc[::-1])
def main():
display_extract_rows_iloc_info()
example_extract_rows_iloc()s
if name == "main":
main()
"""This code includes:
A function display_extract_rows_iloc_info() to display information about extracting rows using Pandas .iloc[].
A function example_extract_rows_iloc() to demonstrate example usage of extracting rows using Pandas .iloc[].
A main() function to call the above functions.
You can run this code to see the output of the extracting rows examples.
Here are some key points to note:
.iloc[] is used to extract rows from a DataFrame based on their position.
The position is 0-based, meaning the first row is at position 0.
You can extract a single row, multiple rows, a range of rows, or rows with a step.
You can also extract rows in reverse order using a negative step.
"""