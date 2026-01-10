# chi_square_test.py

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_chi_square_test(self):
        print("The Chi-Square test is a statistical method used to determine whether there is a significant association between two categorical variables.")
        print("It's a non-parametric test, meaning it doesn't assume a specific distribution for the data.")


# Chi-Square Test for Independence
class ChiSquareTestForIndependence:
    def __init__(self):
        pass

    def describe_chi_square_test_for_independence(self):
        print("The Chi-Square test for independence is used to determine whether there is a significant relationship between two categorical variables.")
        print("Example: Researchers want to see if there is a significant association between income level and subscription status.")

    def calculate_chi_square_statistic(self, observed: np.ndarray) -> float:
        chi2_stat, _, _, _ = stats.chi2_contingency(observed)
        return chi2_stat


# Chi-Square Goodness-of-Fit Test
class ChiSquareGoodnessOfFitTest:
    def __init__(self):
        pass

    def describe_chi_square_goodness_of_fit_test(self):
        print("The Chi-Square goodness-of-fit test is used to determine whether a variable follows a specific expected pattern or distribution.")
        print("Example: Researchers want to see if a six-sided die is fair.")

    def calculate_chi_square_statistic(self, observed: np.ndarray, expected: np.ndarray) -> float:
        chi2_stat = np.sum((observed - expected) ** 2 / expected)
        return chi2_stat


def main():
    print("Chi-Square Test")
    introduction = Introduction()
    introduction.describe_chi_square_test()

    chi_square_test_for_independence = ChiSquareTestForIndependence()
    chi_square_test_for_independence.describe_chi_square_test_for_independence()
    observed = np.array([[20, 30], [40, 25], [10, 15]])
    chi2_stat = chi_square_test_for_independence.calculate_chi_square_statistic(observed)
    print("Chi-Square Statistic:", chi2_stat)

    # Calculate p-value and degrees of freedom
    chi2_stat, p_val, dof, expected = stats.chi2_contingency(observed)
    print("P-value:", p_val)
    print("Degrees of Freedom:", dof)
    print("Expected Frequencies:\n", expected)

    # Critical value for df = 2 and alpha = 0.05
    df = 2
    alpha = 0.05
    critical_value = stats.chi2.ppf(1 - alpha, df)
    print("Critical Value:", critical_value)

    # Plot Chi-Square distribution
    x = np.linspace(0, 10, 1000)
    y = stats.chi2.pdf(x, df)

    plt.plot(x, y, label='Chi-Square Distribution (df=2)')
    plt.fill_between(x, y, where=(x > critical_value), color='red', alpha=0.5, label='Critical Region')
    plt.axvline(chi2_stat, color='blue', linestyle='dashed', label='Calculated Chi-Square')
    plt.axvline(critical_value, color='green', linestyle='dashed', label='Critical Value')
    plt.title('Chi-Square Distribution and Critical Region')
    plt.xlabel('Chi-Square Value')
    plt.ylabel('Probability Density Function')
    plt.legend()
    plt.show()

    # Interpretation
    if chi2_stat > critical_value:
        print("Reject the null hypothesis: There is a significant association between income level and subscription status.")
    else:
        print("Fail to reject the null hypothesis: There is no significant association between income level and subscription status.")


if __name__ == "__main__":
    main()