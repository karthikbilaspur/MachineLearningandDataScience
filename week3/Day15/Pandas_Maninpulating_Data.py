
Here is the complete Python program:

```python
import pandas as pd

def display_filtering_info():
    print("# Filtering #")
    print("-----------")
    print("Filtering is the process of selecting a subset of data based on certain conditions.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    filtered_df = df[df['Age'] > 30]
    print(filtered_df)

def display_sorting_info():
    print("\n# Sorting #")
    print("---------")
    print("Sorting is the process of arranging data in a specific order.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    sorted_df = df.sort_values(by='Age')
    print(sorted_df)

def display_grouping_info():
    print("\n# Grouping #")
    print("----------")
    print("Grouping is the process of splitting data into groups based on some criteria.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32],
            'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df = pd.DataFrame(data)
    grouped_df = df.groupby('Country')['Age'].mean()
    print(grouped_df)

def display_merging_info():
    print("\n# Merging #")
    print("---------")
    print("Merging is the process of combining data from two or more DataFrames.")
    print()
    print("**Example:**")
    data1 = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
             'Age': [28, 24, 35, 32]}
    df1 = pd.DataFrame(data1)
    data2 = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
             'Country': ['USA', 'UK', 'Australia', 'Germany']}
    df2 = pd.DataFrame(data2)
    merged_df = pd.merge(df1, df2, on='Name')
    print(merged_df)

def display_reshaping_info():
    print("\n# Reshaping #")
    print("-----------")
    print("Reshaping is the process of changing the structure of a DataFrame.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'John', 'Anna', 'Anna'],
            'Year': [2018, 2019, 2018, 2019],
            'Sales': [100, 200, 150, 250]}
    df = pd.DataFrame(data)
    pivoted_df = df.pivot(index='Name', columns='Year', values='Sales')
    print(pivoted_df)

def display_melting_info():
    print("\n# Melting #")
    print("---------")
    print("Melting is the process of reshaping data from wide format to long format.")
    print()
    print("**Example:**")
    data = {'Name': ['John', 'Anna'],
            '2018': [100, 150],
            '2019': [200, 250]}
    df = pd.DataFrame(data)
    melted_df = pd.melt(df, id_vars='Name', value_vars=['2018', '2019'])
    print(melted_df)

def main():
    display_filtering_info()
    display_sorting_info()
    display_grouping_info()
    display_merging_info()
    display_reshaping_info()
    display_melting_info()

if __name__ == "__main__":
    main()