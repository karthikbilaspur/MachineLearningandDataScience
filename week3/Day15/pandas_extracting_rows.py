import pandas as pd
def display_extract_rows_loc_info():
# Display information about extracting rows using Pandas .loc[].
print("# Extracting Rows using Pandas .loc[] #")
print("------------------------------------------")
print("The .loc[] method is used to extract rows from a DataFrame based on their label.")
print("It is primarily label based (index values).")
print()
print("Syntax:")
print("df.loc[row_selection, column_selection]")
print()
print("Parameters:")
print("row_selection: A label, a list of labels, or a slice of labels.")
print("column_selection: A label, a list of labels, or a slice of labels.")
def example_extract_rows_loc():
# Example usage of extracting rows using Pandas .loc[].
# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
'Age': [28, 24, 35, 32],
'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])
Code
print("\n# Example 1: Extract a single row #")
print(df.loc['A'])

print("\n# Example 2: Extract multiple rows #")
print(df.loc[['A', 'C']])

print("\n# Example 3: Extract a range of rows #")
print(df.loc['A':'C'])

print("\n# Example 4: Extract rows with a condition #")
print(df.loc[df['Age'] > 30])

print("\n# Example 5: Extract rows and columns #")
print(df.loc[['A', 'C'], ['Name', 'Age']])
def main():
display_extract_rows_loc_info()
example_extract_rows_loc()
if name == "main":
main()

"""This code includes:
A function display_extract_rows_loc_info() to display information about extracting rows using Pandas .loc[].
A function example_extract_rows_loc() to demonstrate example usage of extracting rows using Pandas .loc[].
A main() function to call the above functions.
You can run this code to see the output of the extracting rows examples.
Here are some key points to note:
.loc[] is used to extract rows from a DataFrame based on their label.
The label is the index value of the row.
You can extract a single row, multiple rows, a range of rows, or rows with a condition.
You can also extract rows and columns using .loc[].
Remember to use the correct syntax and parameters to extract the rows you need.
Note: The .loc[] method is label-based, so it will include the end label in the range, unlike the .iloc[] method which is position-based and excludes the end position.
"""