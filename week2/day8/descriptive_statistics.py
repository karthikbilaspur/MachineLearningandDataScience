# descriptive_statistics.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_importance(self):
        print("Descriptive statistics is a branch of statistics that deals with summarizing and describing the features of a dataset.")
        print("It provides an overview of the data, helping to understand the underlying patterns and trends.")
        print("Descriptive statistics is a crucial step in data analysis, as it helps to identify the characteristics of the data and inform further analysis.")


# Types of Descriptive Statistics
class TypesOfDescriptiveStatistics:
    def __init__(self):
        pass

    def describe_types(self):
        print("There are two main types of descriptive statistics:")
        print("1. Measures of Central Tendency:")
        print("   - Mean: The average value of the dataset.")
        print("   - Median: The middle value of the dataset when it is sorted in ascending order.")
        print("   - Mode: The most frequently occurring value in the dataset.")
        print("2. Measures of Variability:")
        print("   - Range: The difference between the maximum and minimum values in the dataset.")
        print("   - Variance: The average of the squared differences from the mean.")
        print("   - Standard Deviation: The square root of the variance.")
        print("   - Interquartile Range (IQR): The difference between the 75th percentile (Q3) and the 25th percentile (Q1).")
        print("   - Coefficient of Variation (CV): The ratio of the standard deviation to the mean.")


# Measures of Central Tendency
class MeasuresOfCentralTendency:
    def __init__(self):
        pass

    def describe_measures(self):
        print("Measures of Central Tendency:")
        print("1. Mean:")
        print("   - The mean is sensitive to outliers and should be used with caution.")
        print("   - It is calculated by summing all the values and dividing by the number of values.")
        print("2. Median:")
        print("   - The median is a more robust measure than the mean and is less affected by outliers.")
        print("   - It is calculated by sorting the data and finding the middle value.")
        print("3. Mode:")
        print("   - The mode is the most frequently occurring value in the dataset.")
        print("   - A dataset can have multiple modes if there are multiple values that occur with the same frequency.")


# Measures of Variability
class MeasuresOfVariability:
    def __init__(self):
        pass

    def describe_measures(self):
        print("Measures of Variability:")
        print("1. Range:")
        print("   - The range is a simple measure of variability, but it is sensitive to outliers.")
        print("   - It is calculated by subtracting the minimum value from the maximum value.")
        print("2. Variance:")
        print("   - The variance is a measure of the average squared difference from the mean.")
        print("   - It is calculated by summing the squared differences from the mean and dividing by the number of values.")
        print("3. Standard Deviation:")
        print("   - The standard deviation is the square root of the variance.")
        print("   - It is a more interpretable measure of variability than the variance.")


# Usage of Descriptive Statistics
class UsageOfDescriptiveStatistics:
    def __init__(self):
        pass

    def describe_usage(self):
        print("Descriptive statistics is used in various ways:")
        print("1. Summarizing data: Descriptive statistics helps to summarize large datasets into a few meaningful numbers.")
        print("2. Identifying patterns: It helps to identify patterns and trends in the data.")
        print("3. Comparing datasets: Descriptive statistics can be used to compare different datasets.")
        print("4. Informing further analysis: It provides insights that can inform further analysis, such as hypothesis testing or predictive modeling.")


# Example of Descriptive Statistics
class ExampleOfDescriptiveStatistics:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def calculate_descriptive_statistics(self):
        mean = sum(self.data) / len(self.data)
        self.data.sort()
        median = self.data[len(self.data) // 2]
        mode = max(set(self.data), key=self.data.count)
        range_ = max(self.data) - min(self.data)
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
        std_dev = variance ** 0.5
        q1 = self.data[len(self.data) // 4]
        q3 = self.data[3 * len(self.data) // 4]
        iqr = q3 - q1
        cv = std_dev / mean

        print("Descriptive Statistics:")
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Mode: {mode}")
        print(f"Range: {range_}")
        print(f"Variance: {variance}")
        print(f"Standard Deviation: {std_dev}")
        print(f"Interquartile Range (IQR): {iqr}")
        print(f"Coefficient of Variation (CV): {cv}")


def main():
    print("Descriptive Statistics")
    introduction = Introduction()
    introduction.describe_importance()

    types_of_descriptive_statistics = TypesOfDescriptiveStatistics()
    types_of_descriptive_statistics.describe_types()

    measures_of_central_tendency = MeasuresOfCentralTendency()
    measures_of_central_tendency.describe_measures()

    measures_of_variability = MeasuresOfVariability()
    measures_of_variability.describe_measures()

    usage_of_descriptive_statistics = UsageOfDescriptiveStatistics()
    usage_of_descriptive_statistics.describe_usage()

    example_of_descriptive_statistics = ExampleOfDescriptiveStatistics()
    example_of_descriptive_statistics.calculate_descriptive_statistics()


if __name__ == "__main__":
    main()