# pandas_tail_method.py

import pandas as pd

def display_tail_method_info():
    """Display information about the tail() method."""
    print("# Pandas tail() Method #")
    print("----------------------")
    print("The tail() method is used to retrieve the last few rows of a DataFrame or Series.")
    print("It's commonly used to verify that data has been loaded correctly, check column names, and inspect the last records.")
    print()
    print("**Syntax:**")
    print("DataFrame.tail(n=5)")
    print("Series.tail(n=5)")
    print()
    print("**Parameter:**")
    print("n: Number of rows to retrieve from the bottom of the DataFrame or Series.")
    print()
    print("**Return:**")
    print("The last n rows of the DataFrame or Series as a new DataFrame or Series.")

def example_tail_method():
    """Example usage of the tail() method."""
    # Load the NBA dataset
    data = pd.read_csv("nba.csv")
    
    print("\n# Example 1: Using tail() with default number of rows #")
    print(data.tail())
    
    print("\n# Example 2: Using tail() with a custom number of rows #")
    print(data.tail(n=7))
    
    print("\n# Example 3: Using tail() on a Series #")
    series = data["Name"]
    print(series.tail(n=5))
    
    print("\n# Example 4: Describing specific columns with tail() #")
    salary_name = data[['Name', 'Salary']].tail()
    print(salary_name)
    
    print("\n# Example 5: Using tail() after sorting a DataFrame #")
    sorted_data = data.sort_values(by='Age', ascending=False)
    bottom_sorted = sorted_data.tail()
    print(bottom_sorted)

def main():
    display_tail_method_info()
    example_tail_method()

if __name__ == "__main__":
    main()