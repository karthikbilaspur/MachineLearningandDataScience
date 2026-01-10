# pandas_describe_method.py

import pandas as pd

def display_describe_method_info():
    """Display information about the describe() method."""
    print("# Pandas describe() Method #")
    print("------------------------")
    print("The describe() method is used to generate descriptive statistics for numeric data in a DataFrame or Series.")
    print("It's commonly used to understand the central tendency, dispersion, and shape of the data.")
    print()
    print("**Syntax:**")
    print("DataFrame.describe(percentiles=None, include=None, exclude=None)")
    print("Series.describe(percentiles=None, include=None, exclude=None)")
    print()
    print("**Parameters:**")
    print("percentiles: List of percentiles to include in the output.")
    print("include: List of data types to include in the output.")
    print("exclude: List of data types to exclude from the output.")
    print()
    print("**Return:**")
    print("A DataFrame or Series with descriptive statistics.")

def example_describe_method():
    """Example usage of the describe() method."""
    # Load the NBA dataset
    data = pd.read_csv("nba.csv")
    
    print("\n# Example 1: Using describe() on a DataFrame #")
    print(data.describe())
    
    print("\n# Example 2: Using describe() on a Series #")
    series = data["Salary"]
    print(series.describe())
    
    print("\n# Example 3: Using describe() with specific percentiles #")
    print(data.describe(percentiles=[0.25, 0.5, 0.75]))
    
    print("\n# Example 4: Using describe() with specific data types #")
    print(data.describe(include=['int64', 'float64']))
    
    print("\n# Example 5: Using describe() to exclude specific data types #")
    print(data.describe(exclude=['object']))

def main():
    display_describe_method_info()
    example_describe_method()

if __name__ == "__main__":
    main()