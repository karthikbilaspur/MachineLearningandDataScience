# pandas_boolean_indexing.py

import pandas as pd

def display_boolean_indexing_info():
    """Display information about boolean indexing in Pandas."""
    print("# Boolean Indexing in Pandas #")
    print("-----------------------------")
    print("Boolean indexing is a technique used to filter data based on conditions.")
    print("It involves creating a boolean mask and using it to select data from the original DataFrame.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    print(df)
    print()
    print("Select rows where Age > 30:")
    mask = df['Age'] > 30
    print(df[mask])

def example_boolean_indexing():
    """Example usage of boolean indexing."""
    # Create a sample DataFrame
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    
    print("\n# Example 1: Select rows where Age > 30 #")
    mask = df['Age'] > 30
    print(df[mask])
    
    print("\n# Example 2: Select rows where Country is USA or UK #")
    mask = (df['Country'] == 'USA') | (df['Country'] == 'UK')
    print(df[mask])
    
    print("\n# Example 3: Select rows where Age is between 25 and 35 #")
    mask = (df['Age'] >= 25) & (df['Age'] <= 35)
    print(df[mask])

def main():
    display_boolean_indexing_info()
    example_boolean_indexing()

if __name__ == "__main__":
    main()