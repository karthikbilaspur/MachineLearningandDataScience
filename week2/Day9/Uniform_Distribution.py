# uniform_distribution.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_importance(self):
        print("The uniform distribution is a continuous probability distribution that models a random variable with a constant probability density function.")
        print("It is widely used in many fields, including science, engineering, and finance, to model random variables with a uniform probability of occurrence.")
        print("The uniform distribution is a fundamental concept in statistics and is often used as a building block for more complex distributions.")


# Uniform Distribution
class UniformDistribution:
    def __init__(self):
        pass

    def describe_uniform_distribution(self):
        print("Uniform Distribution:")
        print("1. Definition:")
        print("   - The uniform distribution is a continuous probability distribution that models a random variable with a constant probability density function.")
        print("   - It is characterized by two parameters: the minimum value (a) and the maximum value (b).")
        print("2. Formula:")
        print("   - The probability density function (PDF) of the uniform distribution is given by:")
        print("     f(x | a, b) = 1 / (b - a)  for a ≤ x ≤ b")
        print("   - where a is the minimum value, b is the maximum value, and x is the value of the random variable.")
        print("3. Properties:")
        print("   - The uniform distribution is a continuous distribution.")
        print("   - The mean is (a + b) / 2 and the variance is (b - a)^2 / 12.")
        print("   - The distribution is symmetric about the mean.")


# Example of Uniform Distribution
class ExampleOfUniformDistribution:
    def __init__(self):
        self.a = 0
        self.b = 10
        self.x = 5

    def calculate_uniform_distribution(self):
        if self.a <= self.x <= self.b:
            probability = 1 / (self.b - self.a)
        else:
            probability = 0
        print("Uniform Distribution:")
        print(f"f({self.x} | {self.a}, {self.b}) = {probability}")


def main():
    print("Uniform Distribution")
    introduction = Introduction()
    introduction.describe_importance()

    uniform_distribution = UniformDistribution()
    uniform_distribution.describe_uniform_distribution()

    print("\nThe formula for the uniform distribution is:")
    print("f(x | a, b) = 1 / (b - a)  for a ≤ x ≤ b")
    print("where:")
    print("  - a is the minimum value")
    print("  - b is the maximum value")
    print("  - x is the value of the random variable")
    print("This formula calculates the probability density of x, given the minimum value a and the maximum value b.")

    example_of_uniform_distribution = ExampleOfUniformDistribution()
    example_of_uniform_distribution.calculate_uniform_distribution()


if __name__ == "__main__":
    main()