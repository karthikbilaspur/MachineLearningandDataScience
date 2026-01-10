import pandas as pd
import numpy as np

def display_apply_info():
    print("# pandas.apply() #")
    print("------------------")
    print("The apply() method applies a function along an axis of the DataFrame.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    def square(x):
        return x ** 2
    print(df['Age'].apply(square))

def display_apply_row_info():
    print("\n# apply function to every row in python dataframe #")
    print("-------------------------------------------------")
    print("The apply() method can be used to apply a function to every row in a DataFrame.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    def sum_row(row):
        return row['Age'] + len(row['Name'])
    print(df.apply(sum_row, axis=1))

def display_series_apply_info():
    print("\n# series.apply() #")
    print("------------------")
    print("The apply() method can be used to apply a function to a Series.")
    print()
    print("**Example:**")
    s = pd.Series([1, 2, 3, 4])
    def square(x):
        return x ** 2
    print(s.apply(square))

def display_aggregate_info():
    print("\n# aggregate() #")
    print("----------------")
    print("The aggregate() method applies one or more operations over the specified axis.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    print(df['Age'].aggregate(['sum', 'mean', 'max', 'min']))

def display_mean_info():
    print("\n# dataframe mean() #")
    print("--------------------")
    print("The mean() method calculates the mean of the values in a DataFrame.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    print(df['Age'].mean())

def display_mad_info():
    print("\n# dataframe mad() #")
    print("------------------")
    print("The mad() method calculates the mean absolute deviation of the values in a DataFrame.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    print(df['Age'].mad())

def display_sem_info():
    print("\n# dataframe.sem() #")
    print("------------------")
    print("The sem() method calculates the standard error of the mean of the values in a DataFrame.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'United Kingdom', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    print(df['Age'].sem())

def display_value_counts_info():
    print("\n# series.value_counts() #")
    print("------------------------")
    print("The value_counts() method returns a Series containing counts of unique rows in the DataFrame.")
    print()
    print("**Example:**")
    s = pd.Series([1, 2, 2, 3, 3, 3])
    print(s.value_counts())

def display_index_value_counts_info():
    print("\n# index_value_counts #")
    print("---------------------")
    print("The index_value_counts method returns a Series containing counts of unique index values in the DataFrame.")
    print()
    print("**Example:**")
    s = pd.Series([1, 2, 2, 3, 3, 3], index=['a', 'b', 'b', 'c', 'c', 'c'])
    print(s.index.value_counts())

def display_lambda_info():
    print("\n# lambda functions #")
    print("------------------")
    print("Lambda functions are small anonymous functions that can be defined inline within a larger expression.")
    print()
    print("**Example:**")
    s = pd.Series([1, 2, 3, 4])
    print(s.apply(lambda x: x ** 2))

def display_dataframe_info():
    print("\n# dataframe #")
    print("-------------")
    print("A DataFrame is a two-dimensional table of data with columns of potentially different types.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    print(df)

def main():
    display_apply_info()
    display_apply_row_info()
    display_series_apply_info()
    display_aggregate_info()
    display_mean_info()
    display_mad_info()
    display_sem_info()
    display_value_counts_info()
    display_index_value_counts_info()
    display_lambda_info()
    display_dataframe_info()

if __name__ == "__main__":
    main()