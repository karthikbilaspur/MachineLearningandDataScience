import pandas as pd

# Working with Dates and Times
def display_date_time_info():
    print("# Working with Dates and Times #")
    print("--------------------------------")
    print("Pandas provides various tools for working with dates and times.")
    print()
    print("**Example:**")
    data = {'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
            'Value': [10, 20, 30]}
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    print("Original DataFrame:")
    print(df)
    print("\nDate Range:")
    print(pd.date_range('2022-01-01', '2022-01-03'))
    print("\nDate Difference:")
    print(df['Date'].max() - df['Date'].min())

# Working with Text Data
def display_text_data_info():
    print("\n# Working with Text Data #")
    print("-------------------------")
    print("Pandas provides various tools for working with text data.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)
    print("\nUppercase Name:")
    df['Name'] = df['Name'].str.upper()
    print(df)
    print("\nContains 'A':")
    print(df['Name'].str.contains('A'))

# Various Functions
def display_functions_info():
    print("\n# Various Functions #")
    print("--------------------")
    print("Pandas provides various functions for data manipulation and analysis.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)
    print("\nMean Age:")
    print(df['Age'].mean())
    print("\nMedian Age:")
    print(df['Age'].median())
    print("\nStandard Deviation of Age:")
    print(df['Age'].std())

def main():
    display_date_time_info()
    display_text_data_info()
    display_functions_info()

if __name__ == "__main__":
    main()