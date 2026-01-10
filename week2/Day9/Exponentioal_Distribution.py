# exponential_distribution.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_importance(self):
        print("The exponential distribution is a continuous probability distribution that models the time between events in a Poisson process.")
        print("It is widely used in many fields, including science, engineering, and finance, to model the time to failure, time to repair, or time between events.")
        print("The exponential distribution is a fundamental concept in statistics and is often used as a building block for more complex distributions.")


# Exponential Distribution
class ExponentialDistribution:
    def __init__(self):
        pass

    def describe_exponential_distribution(self):
        print("Exponential Distribution:")
        print("1. Definition:")
        print("   - The exponential distribution is a continuous probability distribution that models the time between events in a Poisson process.")
        print("   - It is characterized by one parameter: the rate parameter (λ).")
        print("2. Formula:")
        print("   - The probability density function (PDF) of the exponential distribution is given by:")
        print("     f(x | λ) = λe^(-λx)  for x ≥ 0")
        print("   - where λ is the rate parameter and x is the value of the random variable.")
        print("3. Properties:")
        print("   - The exponential distribution is a continuous distribution.")
        print("   - The mean is 1/λ and the variance is 1/λ^2.")
        print("   - The distribution is skewed to the right.")


# Example of Exponential Distribution
class ExampleOfExponentialDistribution:
    def __init__(self):
        self.rate = 2
        self.x = 1

    def calculate_exponential_distribution(self):
        import math
        probability = self.rate * math.exp(-self.rate * self.x)
        print("Exponential Distribution:")
        print(f"f({self.x} | {self.rate}) = {probability}")


def main():
    print("Exponential Distribution")
    introduction = Introduction()
    introduction.describe_importance()

    exponential_distribution = ExponentialDistribution()
    exponential_distribution.describe_exponential_distribution()

    print("\nThe formula for the exponential distribution is:")
    print("f(x | λ) = λe^(-λx)  for x ≥ 0")
    print("where:")
    print("  - λ is the rate parameter")
    print("  - x is the value of the random variable")
    print("This formula calculates the probability density of x, given the rate parameter λ.")

    example_of_exponential_distribution = ExampleOfExponentialDistribution()
    example_of_exponential_distribution.calculate_exponential_distribution()


if __name__ == "__main__":
    main()