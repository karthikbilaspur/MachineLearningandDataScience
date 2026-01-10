# pandas_head_method.py

import pandas as pd

def display_head_method_info():
    """Display information about the head() method."""
    print("# Pandas head() Method #")
    print("----------------------")
    print("The head() method is used to retrieve the first few rows of a DataFrame or Series.")
    print("It's commonly used to verify that data has been loaded correctly, check column names, and inspect the initial records.")
    print()
    print("**Syntax:**")
    print("DataFrame.head(n=5)")
    print("Series.head(n=5)")
    print()
    print("**Parameter:**")
    print("n: Number of rows to retrieve from the top of the DataFrame or Series.")
    print()
    print("**Return:**")
    print("The first n rows of the DataFrame or Series as a new DataFrame or Series.")

def example_head_method():
    """Example usage of the head() method."""
    # Load the NBA dataset
    data = pd.read_csv("nba.csv")
    
    print("\n# Example 1: Using head() with default number of rows #")
    print(data.head())
    
    print("\n# Example 2: Using head() with a custom number of rows #")
    print(data.head(n=7))
    
    print("\n# Example 3: Using head() on a Series #")
    series = data["Name"]
    print(series.head(n=5))
    
    print("\n# Example 4: Describing specific columns with head() #")
    salary_name = data[['Name', 'Salary']].head()
    print(salary_name)
    
    print("\n# Example 5: Using head() after sorting a DataFrame #")
    sorted_data = data.sort_values(by='Age', ascending=True)
    top_sorted = sorted_data.head()
    print(top_sorted)

def main():
    display_head_method_info()
    example_head_method()

if __name__ == "__main__":
    main()