# inferential_statistics.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_importance(self):
        print("Inferential statistics is a branch of statistics that deals with making inferences or conclusions about a population based on a sample of data.")
        print("It involves using statistical methods to make predictions or estimates about a population parameter based on a sample statistic.")
        print("Inferential statistics is used to test hypotheses and make decisions about a population based on a sample of data.")


# Types of Inferential Statistics
class TypesOfInferentialStatistics:
    def __init__(self):
        pass

    def describe_types(self):
        print("There are several types of inferential statistics, including:")
        print("1. Hypothesis Testing:")
        print("   - Hypothesis testing involves testing a hypothesis about a population parameter based on a sample of data.")
        print("   - It involves calculating a test statistic and comparing it to a critical value or p-value.")
        print("2. Confidence Intervals:")
        print("   - Confidence intervals involve estimating a population parameter based on a sample of data.")
        print("   - It involves calculating a range of values within which the population parameter is likely to lie.")
        print("3. Regression Analysis:")
        print("   - Regression analysis involves modeling the relationship between a dependent variable and one or more independent variables.")
        print("   - It involves estimating the coefficients of the regression model and testing hypotheses about the relationships.")


# Hypothesis Testing
class HypothesisTesting:
    def __init__(self):
        pass

    def describe_hypothesis_testing(self):
        print("Hypothesis Testing:")
        print("1. Null Hypothesis:")
        print("   - The null hypothesis is a statement of no effect or no difference.")
        print("   - It is denoted by H0.")
        print("2. Alternative Hypothesis:")
        print("   - The alternative hypothesis is a statement of an effect or difference.")
        print("   - It is denoted by H1.")
        print("3. Test Statistic:")
        print("   - The test statistic is a numerical value that is calculated from the sample data.")
        print("   - It is used to determine whether the null hypothesis should be rejected.")
        print("4. P-Value:")
        print("   - The p-value is the probability of observing a test statistic as extreme or more extreme than the one observed, assuming the null hypothesis is true.")
        print("   - It is used to determine whether the null hypothesis should be rejected.")


# Confidence Intervals
class ConfidenceIntervals:
    def __init__(self):
        pass

    def describe_confidence_intervals(self):
        print("Confidence Intervals:")
        print("1. Point Estimate:")
        print("   - The point estimate is the best estimate of the population parameter based on the sample data.")
        print("   - It is usually the sample mean or proportion.")
        print("2. Margin of Error:")
        print("   - The margin of error is the amount of error that is allowed in the estimate.")
        print("   - It is usually calculated as the standard error times a critical value.")
        print("3. Confidence Level:")
        print("   - The confidence level is the probability that the confidence interval contains the population parameter.")
        print("   - It is usually expressed as a percentage, such as 95%.")


# Example of Inferential Statistics
class ExampleOfInferentialStatistics:
    def __init__(self):
        self.sample_mean = 10
        self.sample_std = 2
        self.sample_size = 100
        self.confidence_level = 0.95

    def calculate_confidence_interval(self):
        import scipy.stats as stats
        std_error = self.sample_std / (self.sample_size ** 0.5)
        critical_value = stats.t.ppf((1 + self.confidence_level) / 2, self.sample_size - 1)
        margin_of_error = critical_value * std_error
        lower_bound = self.sample_mean - margin_of_error
        upper_bound = self.sample_mean + margin_of_error

        print("Confidence Interval:")
        print(f"({lower_bound}, {upper_bound})")


def main():
    print("Inferential Statistics")
    introduction = Introduction()
    introduction.describe_importance()

    types_of_inferential_statistics = TypesOfInferentialStatistics()
    types_of_inferential_statistics.describe_types()

    hypothesis_testing = HypothesisTesting()
    hypothesis_testing.describe_hypothesis_testing()

    confidence_intervals = ConfidenceIntervals()
    confidence_intervals.describe_confidence_intervals()

    example_of_inferential_statistics = ExampleOfInferentialStatistics()
    example_of_inferential_statistics.calculate_confidence_interval()


if __name__ == "__main__":
    main()