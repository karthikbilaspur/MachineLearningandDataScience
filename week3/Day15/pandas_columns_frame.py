pandas_column_slices.py
import pandas as pd
def display_column_slices_info():
"""Display information about column slices in Pandas."""
print("# Column Slices in Pandas #")
print("-------------------------")
print("Column slices are used to select specific columns from a DataFrame.")
print("You can select one or more columns using their names or indices.")
print()
print("Syntax:")
print("df['column_name'] # Select a single column")
print("df[['column1', 'column2']] # Select multiple columns")
print("df.iloc[:, start_index:end_index] # Select columns by index")
print()
print("Example:")
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
'Age': [28, 24, 35, 32],
'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data)
print(df)
print()
print("Select 'Name' column:")
print(df['Name'])
print()
print("Select 'Name' and 'Age' columns:")
print(df[['Name', 'Age']])
print()
print("Select columns by index (1st and 2nd columns):")
print(df.iloc[:, 0:2])
def example_column_slices():
"""Example usage of column slices."""
# Create a sample DataFrame
data = {'Student ID': [1, 2, 3, 4],
'Name': ['John', 'Anna', 'Peter', 'Linda'],
'Age': [20, 21, 19, 22],
'Grade': [85, 90, 78, 92]}
df = pd.DataFrame(data)
Code
print("\n# Example 1: Select a single column #")
print(df['Name'])

print("\n# Example 2: Select multiple columns #")
print(df[['Name', 'Age', 'Grade']])

print("\n# Example 3: Select columns by index #")
print(df.iloc[:, 0:3])

print("\n# Example 4: Select columns using a list of column names #")
columns = ['Name', 'Age', 'Grade']
print(df[columns])

print("\n# Example 5: Select columns using a conditional statement #")
print(df.loc[:, df.dtypes == 'int64'])
def main():
display_column_slices_info()
example_column_slices()
if name == "main":
main()