import pandas as pd

def display_grouping_info():
    print("# Grouping Data #")
    print("----------------")
    print("Grouping data is the process of splitting data into groups based on some criteria.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'John', 'Anna'],
            'Age': [28, 24, 35, 32, 28, 24],
            'Country': ['USA', 'UK', 'Australia', 'Germany', 'USA', 'UK']}
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)
    grouped_df = df.groupby('Country')['Age'].mean()
    print("\nGrouped DataFrame:")
    print(grouped_df)

def display_merging_info():
    print("\n# Merging #")
    print("---------")
    print("Merging is the process of combining data from two or more DataFrames based on a common column.")
    print()
    print("**Example:**")
    data1 = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
             'Age': [28, 24, 35, 32]}
    df1 = pd.DataFrame(data1)
    data2 = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
             'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df2 = pd.DataFrame(data2)
    print("DataFrame 1:")
    print(df1)
    print("\nDataFrame 2:")
    print(df2)
    merged_df = pd.merge(df1, df2, on='Name')
    print("\nMerged DataFrame:")
    print(merged_df)

def display_joining_info():
    print("\n# Joining #")
    print("--------")
    print("Joining is similar to merging, but it combines DataFrames based on their indices.")
    print()
    print("**Example:**")
    data1 = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
             'Age': [28, 24, 35, 32]}
    df1 = pd.DataFrame(data1, index=['A', 'B', 'C', 'D'])
    data2 = {'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df2 = pd.DataFrame(data2, index=['A', 'B', 'C', 'D'])
    print("DataFrame 1:")
    print(df1)
    print("\nDataFrame 2:")
    print(df2)
    joined_df = df1.join(df2)
    print("\nJoined DataFrame:")
    print(joined_df)

def display_concatenating_info():
    print("\n# Concatenating #")
    print("--------------")
    print("Concatenating is the process of combining DataFrames along a particular axis.")
    print()
    print("**Example:**")
    data1 = {'Name': ['John', 'Anna'],
             'Age': [28, 24]}
    df1 = pd.DataFrame(data1)
    data2 = {'Name': ['Peter', 'Linda'],
             'Age': [35, 32]}
    df2 = pd.DataFrame(data2)
    print("DataFrame 1:")
    print(df1)
    print("\nDataFrame 2:")
    print(df2)
    concatenated_df = pd.concat([df1, df2])
    print("\nConcatenated DataFrame:")
    print(concatenated_df)

def main():
    display_grouping_info()
    display_merging_info()
    display_joining_info()
    display_concatenating_info()

if __name__ == "__main__":
    main()s