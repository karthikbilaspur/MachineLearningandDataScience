# confidence_interval.py

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_confidence_interval(self):
        print("A confidence interval is a statistical tool used to estimate the population parameter based on a sample of data.")
        print("It provides a range of values within which the true population parameter is likely to lie.")
        print("The width of the confidence interval gives us an idea of the uncertainty associated with our estimate.")


# Confidence Interval for Mean
class ConfidenceIntervalForMean:
    def __init__(self):
        pass

    def describe_confidence_interval_for_mean(self):
        print("A confidence interval for the mean is used to estimate the population mean based on a sample of data.")
        print("Example: Estimate the average height of adults in a city based on a random sample of 100 adults.")

    def calculate_confidence_interval(self, data, confidence=0.95):
        mean = np.mean(data)
        std_err = stats.sem(data)
        interval = stats.t.interval(confidence, len(data)-1, loc=mean, scale=std_err)
        return interval


# Confidence Interval for Proportion
class ConfidenceIntervalForProportion:
    def __init__(self):
        pass

    def describe_confidence_interval_for_proportion(self):
        print("A confidence interval for the proportion is used to estimate the population proportion based on a sample of data.")
        print("Example: Estimate the proportion of adults in a city who support a particular policy based on a random sample of 1000 adults.")

    def calculate_confidence_interval(self, successes, trials, confidence=0.95):
        proportion = successes / trials
        std_err = np.sqrt(proportion * (1 - proportion) / trials)
        interval = stats.norm.interval(confidence, loc=proportion, scale=std_err)
        return interval


def main():
    print("Confidence Interval")
    introduction = Introduction()
    introduction.describe_confidence_interval()

    confidence_interval_for_mean = ConfidenceIntervalForMean()
    confidence_interval_for_mean.describe_confidence_interval_for_mean()
    data = np.random.normal(10, 2, 100)
    interval = confidence_interval_for_mean.calculate_confidence_interval(data)
    print("Confidence Interval for Mean:", interval)

    confidence_interval_for_proportion = ConfidenceIntervalForProportion()
    confidence_interval_for_proportion.describe_confidence_interval_for_proportion()
    successes = 600
    trials = 1000
    interval = confidence_interval_for_proportion.calculate_confidence_interval(successes, trials)
    print("Confidence Interval for Proportion:", interval)

    print("\nUse Cases:")
    print("1. Estimating Population Parameters: Confidence intervals are used to estimate population parameters, such as the mean or proportion, based on a sample of data.")
    print("2. Hypothesis Testing: Confidence intervals can be used for hypothesis testing by checking if the null hypothesis value falls within the interval.")
    print("3. Comparing Groups: Confidence intervals can be used to compare groups by checking if the intervals overlap or not.")

    print("\nAdvantages:")
    print("1. Easy to Interpret: Confidence intervals are easy to interpret, providing a range of values within which the true population parameter is likely to lie.")
    print("2. Widely Used: Confidence intervals are widely used in statistical analysis, making it easy to find resources and support.")
    print("3. Flexible: Confidence intervals can be used for various types of data and statistical analyses.")

    print("\nDisadvantages:")
    print("1. Assumptions: Confidence intervals assume certain conditions, such as normality of data or independence of observations, which may not always be met.")
    print("2. Sensitive to Sample Size: Confidence intervals are sensitive to sample size, which can affect the width of the interval.")
    print("3. Limited Scope: Confidence intervals are limited to estimating population parameters and may not provide a complete picture of the data.")


if __name__ == "__main__":
    main()