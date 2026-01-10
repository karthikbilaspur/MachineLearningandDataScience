# pandas_programs.py

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

if __name__ == "__main__":
    create_dataframe()
    file_name = 'data.csv'
    read_csv_file(file_name)
    filter_data()