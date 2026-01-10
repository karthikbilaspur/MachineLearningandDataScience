import pandas as pd
def display_indexing_selecting_info():
"""Display information about indexing and selecting data with Pandas."""
print("# Indexing and Selecting Data with Pandas #")
print("------------------------------------------")
print("Pandas provides various ways to index and select data from DataFrames and Series.")
print("Here are some common methods:")
print()
print("* Label-based indexing: .loc[]")
print("* Position-based indexing: .iloc[]")
print("* Boolean indexing: df[df['column'] > value]")
print("* Label-based selection: df.loc[row_label, column_label]")
print("* Position-based selection: df.iloc[row_position, column_position]")
def example_indexing_selecting():
"""Example usage of indexing and selecting data with Pandas."""
# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
'Age': [28, 24, 35, 32],
'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])
Code
print("\n# Example 1: Label-based indexing #")
print(df.loc['A'])

print("\n# Example 2: Position-based indexing #")
print(df.iloc[0])

print("\n# Example 3: Boolean indexing #")
print(df[df['Age'] > 30])

print("\n# Example 4: Label-based selection #")
print(df.loc['A', 'Name'])

print("\n# Example 5: Position-based selection #")
print(df.iloc[0, 1])

print("\n# Example 6: Selecting multiple rows and columns #")
print(df.loc[['A', 'C'], ['Name', 'Age']])

print("\n# Example 7: Selecting a range of rows and columns #")
print(df.loc['A':'C', 'Name':'Age'])
def main():
display_indexing_selecting_info()
example_indexing_selecting()
if name == "main":
main()

"""
This code includes:
A function display_indexing_selecting_info() to display information about indexing and selecting data with Pandas.
A function example_indexing_selecting() to demonstrate example usage of indexing and selecting data with Pandas.
A main() function to call the above functions.
You can run this code to see the output of the indexing and selecting examples.
Here are some key points to note:
.loc[] is used for label-based indexing and selection.
.iloc[] is used for position-based indexing and selection.
Boolean indexing is used to select data based on conditions.
Label-based selection is used to select data using labels.
Position-based selection is used to select data using positions.
"""