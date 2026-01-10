# hypothesis_testing.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_hypothesis_testing(self):
        print("Hypothesis testing compares two opposite ideas about a group of people or things and uses data from a small part of that group (a sample) to decide which idea is more likely true.")
        print("We collect and study the sample data to check if the claim is correct.")


# Defining Hypotheses
class DefiningHypotheses:
    def __init__(self):
        pass

    def describe_hypotheses(self):
        print("Null Hypothesis (H₀): The starting assumption. For example, 'The average visits are 50.'")
        print("Alternative Hypothesis (H₁): The opposite, saying there is a difference. For example, 'The average visits are not 50.'")


# Key Terms
class KeyTerms:
    def __init__(self):
        pass

    def describe_key_terms(self):
        print("Significance Level (α): How sure we want to be before saying the claim is false. Usually, we choose 0.05 (5%).")
        print("p-value: The chance of seeing the data if the null hypothesis is true. If this is less than α, we say the claim is probably false.")
        print("Test Statistic: A number that helps us decide if the data supports or rejects the claim.")
        print("Critical Value: The cutoff point to compare with the test statistic.")
        print("Degrees of freedom: A number that depends on the data size and helps find the critical value.")


# Types of Hypothesis Testing
class TypesOfHypothesisTesting:
    def __init__(self):
        pass

    def describe_types(self):
        print("1. One-Tailed Test: Used when we expect a change in only one direction, either up or down, but not both.")
        print("   - Left-Tailed (Left-Sided) Test: Checks if the value is less than expected.")
        print("   - Right-Tailed (Right-Sided) Test: Checks if the value is greater than expected.")
        print("2. Two-Tailed Test: Used when we want to see if there is a difference in either direction, higher or lower.")


# Example of Hypothesis Testing
class ExampleOfHypothesisTesting:
    def __init__(self):
        import numpy as np
        self.before_treatment = np.array([120, 122, 118, 130, 125, 128, 115, 121, 123, 119])
        self.after_treatment = np.array([115, 120, 112, 128, 122, 125, 110, 117, 119, 114])

    def simulate_hypothesis_testing(self):
        import scipy.stats as stats
        alpha = 0.05
        t_stat, p_val = stats.ttest_rel(self.after_treatment, self.before_treatment)
        decision = "Reject" if p_val <= alpha else "Fail to reject"
        concl = "Significant difference." if decision == "Reject" else "No significant difference."
        print("T:", t_stat)
        print("P:", p_val)
        print(f"Decision: {decision} H0 at α={alpha}")
        print("Conclusion:", concl)


def main():
    print("Hypothesis Testing")
    introduction = Introduction()
    introduction.describe_hypothesis_testing()

    defining_hypotheses = DefiningHypotheses()
    defining_hypotheses.describe_hypotheses()

    key_terms = KeyTerms()
    key_terms.describe_key_terms()

    types_of_hypothesis_testing = TypesOfHypothesisTesting()
    types_of_hypothesis_testing.describe_types()

    example_of_hypothesis_testing = ExampleOfHypothesisTesting()
    example_of_hypothesis_testing.simulate_hypothesis_testing()


if __name__ == "__main__":
    main()