# pandas_programs_new.py

import pandas as pd

def create_dataframe():
    # Create a dictionary
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'City': ['New York', 'Paris', 'Tokyo', 'Sydney']}

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Print the DataFrame
    print("Program 1: Creating a Simple DataFrame")
    print(df)

def read_csv_file(file_name):
    try:
        # Read a CSV file
        df = pd.read_csv(file_name)

        # Print the first 5 rows of the DataFrame
        print("\nProgram 2: Reading a CSV File")
        print(df.head())
    except FileNotFoundError:
        print("File not found. Please check the file name and path.")

def filter_data():
    # Create a dictionary
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'City': ['New York', 'Paris', 'Tokyo', 'Sydney']}

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Filter the DataFrame
    df_filtered = df[df['Age'] > 30]

    # Print the filtered DataFrame
    print("\nProgram 3: Filtering Data")
    print(df_filtered)

def group_by_city():
    # Create a dictionary
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom'],
            'Age': [28, 24, 35, 32, 30],
            'City': ['New York', 'Paris', 'Tokyo', 'Sydney', 'New York']}

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Group by City and calculate mean Age
    df_grouped = df.groupby('City')['Age'].mean()

    # Print the grouped DataFrame
    print("\nProgram 4: Grouping Data by City")
    print(df_grouped)

def merge_dataframes():
    # Create two dictionaries
    data1 = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
             'Age': [28, 24, 35, 32]}
    data2 = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
             'City': ['New York', 'Paris', 'Tokyo', 'Sydney']}

    # Create two DataFrames
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    # Merge the DataFrames
    df_merged = pd.merge(df1, df2, on='Name')

    # Print the merged DataFrame
    print("\nProgram 5: Merging DataFrames")
    print(df_merged)

def sort_data():
    # Create a dictionary
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'City': ['New York', 'Paris', 'Tokyo', 'Sydney']}

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Sort the DataFrame by Age
    df_sorted = df.sort_values(by='Age')

    # Print the sorted DataFrame
    print("\nProgram 6: Sorting Data")
    print(df_sorted)

def pivot_table():
    # Create a dictionary
    data = {'Name': ['John', 'John', 'Anna', 'Anna'],
            'Year': [2018, 2019, 2018, 2019],
            'Sales': [100, 200, 300, 400]}

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Create a pivot table
    df_pivot = pd.pivot_table(df, values='Sales', index='Name', columns='Year')

    # Print the pivot table
    print("\nProgram 7: Creating a Pivot Table")
    print(df_pivot)

def apply_function():
    # Create a dictionary
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32]}

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Apply a function to the Age column
    df['Age'] = df['Age'].apply(lambda x: x + 1)

    # Print the DataFrame with applied function
    print("\nProgram 8: Applying a Function")
    print(df)

def concatenate_dataframes():
    # Create two dictionaries
    data1 = {'Name': ['John', 'Anna'],
             'Age': [28, 24]}
    data2 = {'Name': ['Peter', 'Linda'],
             'Age': [35, 32]}

    # Create two DataFrames
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    # Concatenate the DataFrames
    df_concat = pd.concat([df1, df2])

    # Print the concatenated DataFrame
    print("\nProgram 9: Concatenating DataFrames")
    print(df_concat)

def melt_dataframe():
    # Create a dictionary
    data = {'Name': ['John', 'Anna'],
            '2018': [100, 200],
            '2019': [300, 400]}

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Melt the DataFrame
    df_melt = pd.melt(df, id_vars='Name', var_name='Year', value_name='Sales')

    # Print the melted DataFrame
    print("\nProgram 10: Melting a DataFrame")
    print(df_melt)

if __name__ == "__main__":
    create_dataframe()
    file_name = 'data.csv'
    read_csv_file(file_name)
    filter_data()
    group_by_city()
    merge_dataframes()
    sort_data()
    pivot_table()
    apply_function()
    concatenate_dataframes()
    melt_dataframe()