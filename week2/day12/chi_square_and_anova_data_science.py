# chi_square_anova.py

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_chi_square_anova(self):
        print("Chi-Square and ANOVA are statistical methods used in Data Science to analyze categorical and numerical data.")
        print("Chi-Square is used to determine if there's a significant association between two categorical variables.")
        print("ANOVA is used to compare the means of multiple groups to determine if there's a significant difference.")


# Chi-Square Test
class ChiSquareTest:
    def __init__(self):
        pass

    def describe_chi_square_test(self):
        print("Chi-Square test is used to determine if there's a significant association between two categorical variables.")
        print("Example: Is there a significant association between income level and subscription status?")

    def calculate_chi_square_statistic(self, observed):
        chi2_stat, p_val, dof, expected = stats.chi2_contingency(observed)
        return chi2_stat, p_val, dof, expected


# ANOVA Test
class ANOVATest:
    def __init__(self):
        pass

    def describe_anova_test(self):
        print("ANOVA test is used to compare the means of multiple groups to determine if there's a significant difference.")
        print("Example: Is there a significant difference in the average prices of smartphones from three brands?")

    def calculate_f_statistic(self, *args):
        f_stat, p_val = stats.f_oneway(*args)
        return f_stat, p_val


def main():
    print("Use of Chi-Square and ANOVA in Data Science")
    introduction = Introduction()
    introduction.describe_chi_square_anova()

    chi_square_test = ChiSquareTest()
    chi_square_test.describe_chi_square_test()
    observed = np.array([[20, 30], [40, 25], [10, 15]])
    chi2_stat, p_val, dof, expected = chi_square_test.calculate_chi_square_statistic(observed)
    print("Chi-Square Statistic:", chi2_stat)
    print("P-value:", p_val)
    print("Degrees of Freedom:", dof)
    print("Expected Frequencies:\n", expected)

    anova_test = ANOVATest()
    anova_test.describe_anova_test()
    brand_a = [200, 210, 220, 230, 250]
    brand_b = [180, 190, 200, 210, 220]
    brand_c = [210, 220, 230, 240, 250]
    f_stat, p_val = anova_test.calculate_f_statistic(brand_a, brand_b, brand_c)
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