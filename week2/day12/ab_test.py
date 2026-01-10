# ab_testing.py

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_ab_testing(self):
        print("A/B testing, also known as split testing, is a method of comparing two versions of a product, web page, or application to determine which one performs better.")
        print("It's a statistical experiment that compares the outcomes of two groups: the control group (A) and the treatment group (B).")
        print("The goal of A/B testing is to identify changes that increase a desired outcome, such as clicks, conversions, or sales.")


# A/B Testing
class ABTesting:
    def __init__(self):
        pass

    def describe_ab_testing(self):
        print("A/B testing involves comparing the performance of two versions of a product or web page.")
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
    print("A/B Testing")
    introduction = Introduction()
    introduction.describe_ab_testing()

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
    print("1. Website Optimization: A/B testing is used to optimize website design, layout, and content to improve user engagement and conversion rates.")
    print("2. Marketing Campaigns: A/B testing is used to optimize marketing campaigns by comparing the performance of different ad creatives, targeting options, and bidding strategies.")
    print("3. Product Development: A/B testing is used to optimize product features, pricing, and user experience to improve customer satisfaction and retention.")

    print("\nAdvantages:")
    print("1. Data-Driven Decision Making: A/B testing provides data-driven insights that inform decision making and reduce the risk of costly mistakes.")
    print("2. Improved Conversion Rates: A/B testing helps optimize website design, layout, and content to improve conversion rates and increase revenue.")
    print("3. Reduced Risk: A/B testing reduces the risk of launching a new product or feature by testing it with a small group of users before rolling it out to the entire audience.")

    print("\nDisadvantages:")
    print("1. Limited Scope: A/B testing is limited to testing a single variable or a small set of variables, which may not capture the full complexity of the problem.")
    print("2. Sample Size Requirements: A/B testing requires a large sample size to achieve statistically significant results, which can be time-consuming and expensive.")
    print("3. Interpretation Challenges: A/B testing results can be challenging to interpret, especially when there are multiple variables and interactions involved.")


if __name__ == "__main__":
    main()