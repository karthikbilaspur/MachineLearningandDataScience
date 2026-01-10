# pandas_programs_enhanced.py

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

def handle_missing_values():
    # Create a dictionary
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, None, 32],
            'City': ['New York', 'Paris', 'Tokyo', 'Sydney']}

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Fill missing values with mean Age
    df['Age'] = df['Age'].fillna(df['Age'].mean())

    # Print the DataFrame with filled missing values
    print("\nProgram 6: Handling Missing Values")
    print(df)

if __name__ == "__main__":
    create_dataframe()
    file_name = 'data.csv'
    read_csv_file(file_name)
    filter_data()
    group_by_city()
    merge_dataframes()
    handle_missing_values()