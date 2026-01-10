# normal_distribution.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_importance(self):
        print("The normal distribution, also known as the Gaussian distribution, is a fundamental concept in statistics and probability theory.")
        print("It is a continuous probability distribution that is widely used in many fields, including science, engineering, and finance.")
        print("The normal distribution is a key concept in data analysis and is often used to model real-valued random variables.")


# Normal Distribution
class NormalDistribution:
    def __init__(self):
        pass

    def describe_normal_distribution(self):
        print("Normal Distribution:")
        print("1. Definition:")
        print("   - The normal distribution is a continuous probability distribution that is symmetric about the mean.")
        print("   - It is characterized by two parameters: the mean (μ) and the standard deviation (σ).")
        print("2. Formula:")
        print("   - The probability density function (PDF) of the normal distribution is given by:")
        print("     f(x | μ, σ) = (1 / (σ * sqrt(2 * π))) * exp(-((x - μ) ^ 2) / (2 * σ ^ 2))")
        print("   - where x is the value of the random variable, μ is the mean, and σ is the standard deviation.")
        print("3. Properties:")
        print("   - The normal distribution is symmetric about the mean.")
        print("   - The mean, median, and mode are all equal.")
        print("   - The standard deviation is a measure of the spread of the distribution.")


# Example of Normal Distribution
class ExampleOfNormalDistribution:
    def __init__(self):
        self.mean = 0
        self.std_dev = 1
        self.x = 1.5

    def calculate_normal_distribution(self):
        import numpy as np
        probability = np.exp(-((self.x - self.mean) ** 2) / (2 * self.std_dev ** 2)) / (self.std_dev * np.sqrt(2 * np.pi))
        print("Normal Distribution:")
        print(f"f({self.x} | {self.mean}, {self.std_dev}) = {probability}")


def main():
    print("Normal Distribution")
    introduction = Introduction()
    introduction.describe_importance()

    normal_distribution = NormalDistribution()
    normal_distribution.describe_normal_distribution()

    print("\nThe formula for the normal distribution is:")
    print("f(x | μ, σ) = (1 / (σ * sqrt(2 * π))) * exp(-((x - μ) ^ 2) / (2 * σ ^ 2))")
    print("where:")
    print("x is the value of the random variable")
    print("μ is the mean")
    print("σ is the standard deviation")
    print("π is a mathematical constant approximately equal to 3.14159")
    print("exp is the exponential function")
    print("The normal distribution has several important properties, including:")
    print("Symmetry about the mean")
    print("The mean, median, and mode are all equal")
    print("The standard deviation is a measure of the spread of the distribution")

    example_of_normal_distribution = ExampleOfNormalDistribution()
    example_of_normal_distribution.calculate_normal_distribution()


if __name__ == "__main__":
    main()