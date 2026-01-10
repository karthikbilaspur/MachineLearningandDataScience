
import pandas as pd

# Writing CSV Files
def display_write_csv_info():
    print("# Writing CSV Files #")
    print("--------------------")
    print("Pandas provides the `to_csv()` function to write DataFrames to CSV files.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)
    df.to_csv('example.csv', index=False)
    print("\nCSV file written successfully.")

# Reading CSV Files
def display_read_csv_info():
    print("\n# Reading CSV Files #")
    print("--------------------")
    print("Pandas provides the `read_csv()` function to read CSV files into DataFrames.")
    print()
    print("**Example:**")
    df = pd.read_csv('example.csv')
    print("CSV file contents:")
    print(df)

# Writing Excel Files
def display_write_excel_info():
    print("\n# Writing Excel Files #")
    print("----------------------")
    print("Pandas provides the `to_excel()` function to write DataFrames to Excel files.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)
    df.to_excel('example.xlsx', index=False)
    print("\nExcel file written successfully.")

# Reading Excel Files
def display_read_excel_info():
    print("\n# Reading Excel Files #")
    print("----------------------")
    print("Pandas provides the `read_excel()` function to read Excel files into DataFrames.")
    print()
    print("**Example:**")
    df = pd.read_excel('example.xlsx')
    print("Excel file contents:")
    print(df)

def main():
    display_write_csv_info()
    display_read_csv_info()
    display_write_excel_info()
    display_read_excel_info()

if __name__ == "__main__":
    main()
"""
This code includes:
A function display_write_csv_info() to display information about writing CSV files.
A function display_read_csv_info() to display information about reading CSV files.
A function display_write_excel_info() to display information about writing Excel files.
A function display_read_excel_info() to display information about reading Excel files.
A main() function to call the above functions.
You can run this code to see the output of the examples.
Here are some key points to note:
Pandas provides the to_csv() function to write DataFrames to CSV files.
Pandas provides the read_csv() function to read CSV files into DataFrames.
Pandas provides the to_excel() function to write DataFrames to Excel files.
Pandas provides the read_excel() function to read Excel files into DataFrames.
Notse: Make sure to install the openpyxl library if you want to work with Excel files. You can install it using pip: pip install openpyxl
"""