# pandas_df_series.py

import pandas as pd
import numpy as np

def display_pandas_df_series_info():
    """Display information about Pandas DataFrame and Series."""
    print("# Pandas DataFrame and Series #")
    print("----------------------------")
    print("**Pandas DataFrame**")
    print("A Pandas DataFrame is a two-dimensional table of data with columns of potentially different types.")
    print("It's similar to an Excel spreadsheet or a table in a relational database.")
    print()
    print("**Example**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    print(df)
    print()
    print("**Pandas Series**")
    print("A Pandas Series is a one-dimensional labeled array of values.")
    print("It's similar to a column in a spreadsheet or a column in a relational database table.")
    print()
    print("**Example**")
    s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
    print(s)

def create_pandas_series():
    """Create Pandas Series from different data structures."""
    print("\n# Creating a Pandas Series #")
    print("-------------------------")
    print("You can create a Pandas Series from:")
    print("*   A Python list")
    print("*   A NumPy array")
    print("*   A scalar value")
    print("*   A dictionary")
    
    # Create Series from a list
    s1 = pd.Series([1, 2, 3, 4, 5])
    print("\nSeries from a list:")
    print(s1)
    
    # Create Series from a NumPy array
    s2 = pd.Series(np.array([1, 2, 3, 4, 5]))
    print("\nSeries from a NumPy array:")
    print(s2)
    
    # Create Series from a scalar value
    s3 = pd.Series(5, index=['a', 'b', 'c'])
    print("\nSeries from a scalar value:")
    print(s3)
    
    # Create Series from a dictionary
    s4 = pd.Series({'a': 1, 'b': 2, 'c': 3})
    print("\nSeries from a dictionary:")
    print(s4)

def create_pandas_df():
    """Create Pandas DataFrame from different data structures."""
    print("\n# Creating a Pandas DataFrame #")
    print("--------------------------")
    print("You can create a Pandas DataFrame from:")
    print("*   A dictionary of lists")
    print("*   A list of dictionaries")
    print("*   A NumPy array")
    print("*   A Pandas Series")
    print("*   A CSV file")
    print("*   An Excel file")
    print("*   A SQL database")
    
    # Create DataFrame from a dictionary of lists
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df1 = pd.DataFrame(data)
    print("\nDataFrame from a dictionary of lists:")
    print(df1)
    
    # Create DataFrame from a list of dictionaries
    data = [{'Name': 'John', 'Age': 28, 'Country': 'USA'},
            {'Name': 'Anna', 'Age': 24, 'Country': 'UK'},
            {'Name': 'Peter', 'Age': 35, 'Country': 'Australia'},
            {'Name': 'Linda', 'Age': 32, 'Country': 'Germany'}]
    df2 = pd.DataFrame(data)
    print("\nDataFrame from a list of dictionaries:")
    print(df2)

def main():
    display_pandas_df_series_info()
    create_pandas_series()
    create_pandas_df()

if __name__ == "__main__":
    main()