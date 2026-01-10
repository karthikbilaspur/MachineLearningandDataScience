# pandas_info.py

import pandas as pd

def display_pandas_info():
    print("# Pandas Information #")
    print("------------------------")
    print("**What is Pandas?**")
    print("Pandas is an open-source library in Python that provides data structures and data analysis tools for efficiently handling structured data.")
    print()
    print("**History of Pandas**")
    print("*   Created by Wes McKinney in 2008")
    print("*   Initially designed for financial time series data")
    print("*   Now a widely-used library in data science and analytics")
    print()
    print("**Advantages of Pandas**")
    print("*   **Efficient Data Structures**: Pandas provides data structures like Series and DataFrame")
    print("*   **Data Manipulation**: Various methods for filtering, sorting, grouping, and merging data")
    print("*   **Data Analysis**: Integrated tools for data analysis, including handling missing data and data merging")
    print()
    print("**Real-Life Applications of Pandas**")
    print("*   **Data Analysis and Science**: Pandas is widely used in data analysis, machine learning, and scientific computing")
    print("*   **Finance**: Used in financial data analysis, risk management, and portfolio optimization")
    print("*   **Statistics**: Used in statistical modeling, data visualization, and hypothesis testing")

def pandas_example():
    print("\n# Pandas Example #")
    print("-----------------")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    print(df)
    print("\nMean Age:", df['Age'].mean())
    print("Count of People:", len(df))

def main():
    display_pandas_info()
    pandas_example()

if __name__ == "__main__":
    main()