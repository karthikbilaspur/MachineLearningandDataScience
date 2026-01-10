pandas_dataframe_ix.py
import pandas as pd
def display_dataframe_ix_info():
"""Display information about DataFrame.ix[] method."""
print("# Pandas DataFrame.ix[] Method #")
print("--------------------------------")
print("The DataFrame.ix[] method is used to access a group of rows and columns by label(s) or a boolean array.")
print("It is label-based, but may also be used with a boolean array.")
print()
print("Syntax:")
print("DataFrame.ix[row_selection, column_selection]")
print()
print("Parameters:")
print("row_selection: A label, a list of labels, a slice of labels, or a boolean array.")
print("column_selection: A label, a list of labels, a slice of labels, or a boolean array.")
print()
print("Return:")
print("A DataFrame or Series with the selected rows and columns.")
def example_dataframe_ix():
"""Example usage of DataFrame.ix[] method."""
# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
'Age': [28, 24, 35, 32],
'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])
Code
print("\n# Example 1: Access a single row #")
print(df.ix['A'])

print("\n# Example 2: Access multiple rows #")
print(df.ix[['A', 'C']])

print("\n# Example 3: Access a single column #")
print(df.ix[:, 'Name'])

print("\n# Example 4: Access multiple columns #")
print(df.ix[:, ['Name', 'Age']])

print("\n# Example 5: Access a range of rows and columns #")
print(df.ix['A':'C', 'Name':'Age'])
def main():
display_dataframe_ix_info()
example_dataframe_ix()
if name == "main":
main()