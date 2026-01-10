# skewness.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_importance(self):
        print("Skewness is a measure of the asymmetry of the probability distribution of a real-valued random variable.")
        print("It is an important concept in statistics and is used to describe the shape of a distribution.")
        print("Skewness can be used to identify outliers and to determine the type of distribution.")


# Methods of Measuring Skewness
class MethodsOfMeasuringSkewness:
    def __init__(self):
        pass

    def describe_methods(self):
        print("Methods of Measuring Skewness:")
        print("1. Visual Inspection:")
        print("   - Visual inspection involves plotting the data and observing the shape of the distribution.")
        print("   - If the distribution is symmetric, it is not skewed.")
        print("   - If the distribution is not symmetric, it is skewed.")
        print("2. Skewness Coefficient:")
        print("   - The skewness coefficient is a numerical measure of skewness.")
        print("   - It is calculated as the third standardized moment.")
        print("   - A skewness coefficient of zero indicates a symmetric distribution.")
        print("   - A positive skewness coefficient indicates a right-skewed distribution.")
        print("   - A negative skewness coefficient indicates a left-skewed distribution.")
        print("3. Skewness Based on Quartiles:")
        print("   - Skewness based on quartiles is a measure of skewness that uses the quartiles of the distribution.")
        print("   - It is calculated as (Q3 + Q1 - 2Q2) / (Q3 - Q1).")
        print("   - A skewness value of zero indicates a symmetric distribution.")
        print("   - A positive skewness value indicates a right-skewed distribution.")
        print("   - A negative skewness value indicates a left-skewed distribution.")


# Karl Pearson Measure
class KarlPearsonMeasure:
    def __init__(self):
        pass

    def describe_karl_pearson_measure(self):
        print("Karl Pearson Measure:")
        print("1. Definition:")
        print("   - The Karl Pearson measure of skewness is a measure of skewness that uses the mean, median, and standard deviation.")
        print("   - It is calculated as 3(Mean - Median) / Standard Deviation.")
        print("   - A Karl Pearson measure of zero indicates a symmetric distribution.")
        print("   - A positive Karl Pearson measure indicates a right-skewed distribution.")
        print("   - A negative Karl Pearson measure indicates a left-skewed distribution.")


# Bowley's Measure
class BowleyMeasure:
    def __init__(self):
        pass

    def describe_bowley_measure(self):
        print("Bowley's Measure:")
        print("1. Definition:")
        print("   - Bowley's measure of skewness is a measure of skewness that uses the quartiles.")
        print("   - It is calculated as (Q3 + Q1 - 2Q2) / (Q3 - Q1).")
        print("   - A Bowley measure of zero indicates a symmetric distribution.")
        print("   - A positive Bowley measure indicates a right-skewed distribution.")
        print("   - A negative Bowley measure indicates a left-skewed distribution.")


# Kelly's Measure
class KellyMeasure:
    def __init__(self):
        pass

    def describe_kelly_measure(self):
        print("Kelly's Measure:")
        print("1. Definition:")
        print("   - Kelly's measure of skewness is a measure of skewness that uses the percentiles.")
        print("   - It is calculated as (P90 + P10 - 2P50) / (P90 - P10).")
        print("   - A Kelly measure of zero indicates a symmetric distribution.")
        print("   - A positive Kelly measure indicates a right-skewed distribution.")
        print("   - A negative Kelly measure indicates a left-skewed distribution.")


# Example of Skewness
class ExampleOfSkewness:
    def __init__(self):
        import numpy as np
        self.data_right_skewed = np.random.exponential(scale=1, size=1000)
        self.data_left_skewed = -np.random.exponential(scale=1, size=1000)
        self.data_symmetric = np.random.normal(loc=0, scale=1, size=1000)

    def calculate_skewness(self):
        import scipy.stats as stats
        skewness_right = stats.skew(self.data_right_skewed)
        skewness_left = stats.skew(self.data_left_skewed)
        skewness_symmetric = stats.skew(self.data_symmetric)
        print("Skewness:")
        print(f"Right Skewed: {skewness_right}")
        print(f"Left Skewed: {skewness_left}")
        print(f"Symmetric: {skewness_symmetric}")


def main():
    print("Skewness")
    introduction = Introduction()
    introduction.describe_importance()

    methods_of_measuring_skewness = MethodsOfMeasuringSkewness()
    methods_of_measuring_skewness.describe_methods()

    karl_pearson_measure = KarlPearsonMeasure()
    karl_pearson_measure.describe_karl_pearson_measure()

    bowley_measure = BowleyMeasure()
    bowley_measure.describe_bowley_measure()

    kelly_measure = KellyMeasure()
    kelly_measure.describe_kelly_measure()

    example_of_skewness = ExampleOfSkewness()
    example_of_skewness.calculate_skewness()


if __name__ == "__main__":
    main()