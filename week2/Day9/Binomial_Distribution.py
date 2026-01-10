# binomial_distribution.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_importance(self):
        print("The binomial distribution is a discrete probability distribution that models the number of successes in a fixed number of independent trials.")
        print("It is widely used in many fields, including science, engineering, and finance, to model binary outcomes such as success/failure, yes/no, or 0/1.")
        print("The binomial distribution is a fundamental concept in statistics and is often used as a building block for more complex distributions.")


# Binomial Distribution
class BinomialDistribution:
    def __init__(self):
        pass

    def describe_binomial_distribution(self):
        print("Binomial Distribution:")
        print("1. Definition:")
        print("   - The binomial distribution is a discrete probability distribution that models the number of successes in a fixed number of independent trials.")
        print("   - It is characterized by two parameters: the number of trials (n) and the probability of success (p).")
        print("2. Formula:")
        print("   - The probability mass function (PMF) of the binomial distribution is given by:")
        print("     P(X=k) = (nCk) * (p^k) * (1-p)^(n-k)")
        print("   - where n is the number of trials, k is the number of successes, p is the probability of success, and nCk is the number of combinations of n items taken k at a time.")
        print("3. Properties:")
        print("   - The binomial distribution is a discrete distribution.")
        print("   - The mean is np and the variance is np(1-p).")
        print("   - The distribution is symmetric if p=0.5 and skewed otherwise.")


# Example of Binomial Distribution
class ExampleOfBinomialDistribution:
    def __init__(self):
        self.n = 10
        self.p = 0.5
        self.k = 6

    def calculate_binomial_distribution(self):
        import math
        nCk = math.comb(self.n, self.k)
        probability = nCk * (self.p ** self.k) * ((1 - self.p) ** (self.n - self.k))
        print("Binomial Distribution:")
        print(f"P(X={self.k}) = {probability}")


def main():
    print("Binomial Distribution")
    introduction = Introduction()
    introduction.describe_importance()

    binomial_distribution = BinomialDistribution()
    binomial_distribution.describe_binomial_distribution()

    print("\nThe formula for the binomial distribution is:")
    print("P(X=k) = (nCk) * (p^k) * (1-p)^(n-k)")
    print("where:")
    print("  - n is the number of trials")
    print("  - k is the number of successes")
    print("  - p is the probability of success")
    print("  - nCk is the number of combinations of n items taken k at a time")
    print("This formula calculates the probability of k successes in n independent trials, where the probability of success is p.")

    example_of_binomial_distribution = ExampleOfBinomialDistribution()
    example_of_binomial_distribution.calculate_binomial_distribution()


if __name__ == "__main__":
    main()