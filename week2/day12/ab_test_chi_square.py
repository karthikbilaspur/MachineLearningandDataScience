# chi_square_ab_test.py

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_chi_square_ab_test(self):
        print("Chi-Square Test and A/B Testing are statistical methods used to analyze categorical data and compare the performance of two groups.")
        print("Chi-Square Test is used to determine if there's a significant association between two categorical variables.")
        print("A/B Testing is used to compare the performance of two versions of a product, web page, or application to determine which one performs better.")


# Chi-Square Test
class ChiSquareTest:
    def __init__(self):
        pass

    def describe_chi_square_test(self):
        print("Chi-Square Test is used to determine if there's a significant association between two categorical variables.")
        print("Example: Is there a significant association between income level and subscription status?")

    def calculate_chi_square_statistic(self, observed):
        chi2_stat, p_val, dof, expected = stats.chi2_contingency(observed)
        return chi2_stat, p_val, dof, expected


# A/B Testing
class ABTesting:
    def __init__(self):
        pass

    def describe_ab_testing(self):
        print("A/B Testing is used to compare the performance of two versions of a product, web page, or application to determine which one performs better.")
        print("Example: Compare the click-through rates of two different button colors on a website.")

    def calculate_p_value(self, successes_a, trials_a, successes_b, trials_b):
        # Calculate the proportions
        prop_a = successes_a / trials_a
        prop_b = successes_b / trials_b

        # Calculate the pooled proportion
        pooled_prop = (successes_a + successes_b) / (trials_a + trials_b)

        # Calculate the standard error
        std_err = np.sqrt(pooled_prop * (1 - pooled_prop) * (1/trials_a + 1/trials_b))

        # Calculate the z-score
        z_score = (prop_a - prop_b) / std_err

        # Calculate the p-value
        p_value = 2 * (1 - stats.norm.cdf(np.abs(z_score)))

        return p_value


def main():
    print("Chi-Square Test and A/B Testing")
    introduction = Introduction()
    introduction.describe_chi_square_ab_test()

    chi_square_test = ChiSquareTest()
    chi_square_test.describe_chi_square_test()
    observed = np.array([[20, 30], [40, 25], [10, 15]])
    chi2_stat, p_val, dof, expected = chi_square_test.calculate_chi_square_statistic(observed)
    print("Chi-Square Statistic:", chi2_stat)
    print("P-value:", p_val)
    print("Degrees of Freedom:", dof)
    print("Expected Frequencies:\n", expected)

    ab_testing = ABTesting()
    ab_testing.describe_ab_testing()
    successes_a = 100
    trials_a = 1000
    successes_b = 120
    trials_b = 1000
    p_value = ab_testing.calculate_p_value(successes_a, trials_a, successes_b, trials_b)
    print("P-value:", p_value)

    # Interpret the results
    alpha = 0.05
    if p_value < alpha:
        print("Reject the null hypothesis: There is a statistically significant difference between the two groups.")
    else:
        print("Fail to reject the null hypothesis: There is no statistically significant difference between the two groups.")

    print("\nUse Cases:")
    print("1. Feature Selection: Chi-Square Test is used for feature selection in machine learning models.")
    print("2. Website Optimization: A/B Testing is used to optimize website design, layout, and content to improve user engagement and conversion rates.")
    print("3. Marketing Campaigns: A/B Testing is used to optimize marketing campaigns by comparing the performance of different ad creatives, targeting options, and bidding strategies.")

    print("\nAdvantages:")
    print("1. Data-Driven Decision Making: Chi-Square Test and A/B Testing provide data-driven insights that inform decision making and reduce the risk of costly mistakes.")
    print("2. Improved Conversion Rates: A/B Testing helps optimize website design, layout, and content to improve conversion rates and increase revenue.")
    print("3. Reduced Risk: A/B Testing reduces the risk of launching a new product or feature by testing it with a small group of users before rolling it out to the entire audience.")

    print("\nDisadvantages:")
    print("1. Limited Scope: Chi-Square Test and A/B Testing are limited to analyzing categorical data and comparing the performance of two groups, respectively.")
    print("2. Sample Size Requirements: A/B Testing requires a large sample size to achieve statistically significant results, which can be time-consuming and expensive.")
    print("3. Interpretation Challenges: A/B Testing results can be challenging to interpret, especially when there are multiple variables and interactions involved.")


if __name__ == "__main__":
    main()