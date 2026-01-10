# statistics_foundation.py

# Basic Statistical Terms
class StatisticalTerms:
    def __init__(self):
        self.data = None
        self.variable = None
        self.population = None
        self.sample = None
        self.parameter = None
        self.statistic = None

    def describe_terms(self):
        print("Data: Facts, numbers or observations collected for analysis.")
        print("  Example: A company's sales data for the past year.")
        print("Variable: Building blocks of statistical analysis.")
        print("  Example: Age, income, temperature, etc.")
        print("Population: Complete set of individuals, objects or data points of interest in a study.")
        print("  Example: All customers of a company.")
        print("Sample: Subset of the population selected for analysis.")
        print("  Example: 1000 customers randomly selected from the company's database.")
        print("Parameter: Numerical value that describes a characteristic of a population.")
        print("  Example: The average income of all customers in the city.")
        print("Statistic: Numerical value that describes a characteristic of a sample.")
        print("  Example: The average income of the 1000 customers surveyed.")


# Types of Statistics
class StatisticsTypes:
    def __init__(self):
        self.descriptive_statistics = None
        self.inferential_statistics = None

    def describe_types(self):
        print("1. Descriptive Statistics: Summarize and describe the main features of a dataset.")
        print("  Example: Calculating the mean, median, and standard deviation of a company's sales data.")
        print("2. Inferential Statistics: Make predictions or inferences about a population based on sample data.")
        print("  Example: Using a sample of 1000 customers to estimate the average income of all customers in the city.")


# Types of Data
class DataTypes:
    def __init__(self):
        self.quantitative_data = None
        self.qualitative_data = None

    def describe_types(self):
        print("1. Quantitative Data: Numerical values that can be measured.")
        print("   - Discrete Data: Countable values that cannot be divided into smaller parts.")
        print("     Example: Number of employees in a company.")
        print("   - Continuous Data: Measurable values that can take any value within a range.")
        print("     Example: Height, weight, temperature.")
        print("2. Qualitative Data: Describes qualities or characteristics and is non-numerical.")
        print("   - Nominal Data: Categories without any inherent order.")
        print("     Example: Colors (red, blue, green), types of fruits (apple, banana, orange).")
        print("   - Ordinal Data: Categories with a meaningful order or ranking.")
        print("     Example: Education levels (high school, bachelor's, master's), customer satisfaction ratings (poor, fair, good, excellent).")


# Levels of Measurement
class MeasurementLevels:
    def __init__(self):
        self.nominal_level = None
        self.ordinal_level = None
        self.interval_level = None
        self.ratio_level = None

    def describe_levels(self):
        print("1. Nominal Level: Categorizing data into distinct groups or labels without any order or ranking.")
        print("  Example: Colors (red, blue, green), types of fruits (apple, banana, orange).")
        print("2. Ordinal Level: Builds on nominal data by introducing order or ranking.")
        print("  Example: Education levels (high school, bachelor's, master's), customer satisfaction ratings (poor, fair, good, excellent).")
        print("3. Interval Level: Numerical and the differences between values are meaningful.")
        print("  Example: Temperature in Celsius or Fahrenheit, IQ scores.")
        print("4. Ratio Level: Has all the properties of interval data, plus a true zero point.")
        print("  Example: Height, weight, income, number of employees.")


def main():
    print("Statistics: The Foundation of Data Science & Analytics")
    statistical_terms = StatisticalTerms()
    statistical_terms.describe_terms()

    statistics_types = StatisticsTypes()
    statistics_types.describe_types()

    data_types = DataTypes()
    data_types.describe_types()

    measurement_levels = MeasurementLevels()
    measurement_levels.describe_levels()


if __name__ == "__main__":
    main()