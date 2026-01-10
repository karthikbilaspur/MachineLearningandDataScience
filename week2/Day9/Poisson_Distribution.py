# poisson_distribution.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_importance(self):
        print("The Poisson distribution is a discrete probability distribution that models the number of events occurring in a fixed interval of time or space.")
        print("It is widely used in many fields, including science, engineering, and finance, to model the number of events such as phone calls, accidents, or defects.")
        print("The Poisson distribution is a fundamental concept in statistics and is often used as a building block for more complex distributions.")


# Poisson Distribution
class PoissonDistribution:
    def __init__(self):
        pass

    def describe_poisson_distribution(self):
        print("Poisson Distribution:")
        print("1. Definition:")
        print("   - The Poisson distribution is a discrete probability distribution that models the number of events occurring in a fixed interval of time or space.")
        print("   - It is characterized by one parameter: the rate parameter (λ).")
        print("2. Formula:")
        print("   - The probability mass function (PMF) of the Poisson distribution is given by:")
        print("     P(X=k) = (e^(-λ) * (λ^k)) / k!")
        print("   - where λ is the rate parameter, k is the number of events, and e is the base of the natural logarithm.")
        print("3. Properties:")
        print("   - The Poisson distribution is a discrete distribution.")
        print("   - The mean is λ and the variance is λ.")
        print("   - The distribution is skewed to the right.")


# Usage in Data Science
class UsageInDataScience:
    def __init__(self):
        pass

    def describe_usage(self):
        print("Usage in Data Science:")
        print("1. Modeling count data: The Poisson distribution is widely used to model count data, such as the number of customers arriving at a store or the number of defects in a manufacturing process.")
        print("2. Predicting rare events: The Poisson distribution can be used to predict the probability of rare events, such as the number of accidents or the number of natural disasters.")
        print("3. Analyzing time series data: The Poisson distribution can be used to analyze time series data, such as the number of website visitors or the number of sales.")
        print("4. Hypothesis testing: The Poisson distribution can be used to test hypotheses about the rate parameter λ.")


# Real-Life Applications
class RealLifeApplications:
    def __init__(self):
        pass

    def describe_applications(self):
        print("Real-Life Applications:")
        print("1. Insurance: The Poisson distribution is used to model the number of claims made by policyholders.")
        print("2. Manufacturing: The Poisson distribution is used to model the number of defects in a manufacturing process.")
        print("3. Finance: The Poisson distribution is used to model the number of trades made in a given time period.")
        print("4. Healthcare: The Poisson distribution is used to model the number of patients arriving at a hospital or the number of diseases occurring in a population.")
        print("5. Traffic engineering: The Poisson distribution is used to model the number of vehicles arriving at an intersection or the number of accidents occurring on a road.")


# Example of Poisson Distribution
class ExampleOfPoissonDistribution:
    def __init__(self):
        self.rate = 2
        self.k = 3

    def calculate_poisson_distribution(self):
        import math
        probability = (math.exp(-self.rate) * (self.rate ** self.k)) / math.factorial(self.k)
        print("Poisson Distribution:")
        print(f"P(X={self.k}) = {probability}")


def main():
    print("Poisson Distribution")
    introduction = Introduction()
    introduction.describe_importance()

    poisson_distribution = PoissonDistribution()
    poisson_distribution.describe_poisson_distribution()

    usage_in_data_science = UsageInDataScience()
    usage_in_data_science.describe_usage()

    real_life_applications = RealLifeApplications()
    real_life_applications.describe_applications()

    print("\nThe formula for the Poisson distribution is:")
    print("P(X=k) = (e^(-λ) * (λ^k)) / k!")
    print("where:")
    print("  - λ is the rate parameter")
    print("  - k is the number of events")
    print("  - e is the base of the natural logarithm")
    print("This formula calculates the probability of k events occurring in a fixed interval of time or space, given the rate parameter λ.")

    example_of_poisson_distribution = ExampleOfPoissonDistribution()
    example_of_poisson_distribution.calculate_poisson_distribution()


if __name__ == "__main__":
    main()