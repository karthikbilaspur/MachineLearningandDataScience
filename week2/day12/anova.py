# anova_test.py

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_anova_test(self):
        print("ANOVA (Analysis of Variance) is a statistical method used to compare the means of multiple groups.")
        print("It's used to determine if there's a significant difference between the means of three or more groups.")


# One-Way ANOVA
class OneWayANOVA:
    def __init__(self):
        pass

    def describe_one_way_anova(self):
        print("One-way ANOVA is used to compare the means of three or more groups based on one independent variable.")
        print("Example: Comparing the average prices of smartphones from three brands: Brand A, Brand B, and Brand C.")

    def calculate_f_statistic(self, *args):
        f_stat, p_val = stats.f_oneway(*args)
        return f_stat, p_val


# Two-Way ANOVA
class TwoWayANOVA:
    def __init__(self):
        pass

    def describe_two_way_anova(self):
        print("Two-way ANOVA is used to compare the means of three or more groups based on two independent variables.")
        print("Example: Comparing the average prices of smartphones from three brands and two storage capacities.")

    def calculate_f_statistic(self, data):
        # Note: scipy.stats does not have a built-in function for two-way ANOVA.
        # We'll use a simple example with stats.f_oneway for demonstration purposes.
        f_stat, p_val = stats.f_oneway(*data)
        return f_stat, p_val


def main():
    print("ANOVA Test")
    introduction = Introduction()
    introduction.describe_anova_test()

    one_way_anova = OneWayANOVA()
    one_way_anova.describe_one_way_anova()
    brand_a = [200, 210, 220, 230, 250]
    brand_b = [180, 190, 200, 210, 220]
    brand_c = [210, 220, 230, 240, 250]
    f_stat, p_val = one_way_anova.calculate_f_statistic(brand_a, brand_b, brand_c)
    print("F-statistic:", f_stat)
    print("P-value:", p_val)

    # Critical value for df = 2 and alpha = 0.05
    df = 2
    alpha = 0.05
    critical_value = stats.f.ppf(1 - alpha, df, 12)
    print("Critical Value:", critical_value)

    # Plot F-distribution
    x = np.linspace(0, 10, 1000)
    y = stats.f.pdf(x, df, 12)

    plt.plot(x, y, label='F-Distribution (df=2, df=12)')
    plt.fill_between(x, y, where=(x > critical_value), color='red', alpha=0.5, label='Critical Region')
    plt.axvline(f_stat, color='blue', linestyle='dashed', label='Calculated F-statistic')
    plt.axvline(critical_value, color='green', linestyle='dashed', label='Critical Value')
    plt.title('F-Distribution and Critical Region')
    plt.xlabel('F-statistic')
    plt.ylabel('Probability Density Function')
    plt.legend()
    plt.show()

    # Interpretation
    if f_stat > critical_value:
        print("Reject the null hypothesis: There is a significant difference between the means of the groups.")
    else:
        print("Fail to reject the null hypothesis: There is no significant difference between the means of the groups.")


if __name__ == "__main__":
    main()