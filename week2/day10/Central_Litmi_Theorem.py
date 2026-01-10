# central_limit_theorem.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_clt(self):
        print("The Central Limit Theorem (CLT) states that if we take many random samples from any population and calculate their averages,")
        print("those averages will form a bell-shaped (normal) curve even if the original data is not normally distributed,")
        print("as long as the sample size is large enough.")


# CLT Formula
class CLTFormula:
    def __init__(self):
        pass

    def describe_clt_formula(self):
        print("CLT Formula:")
        print("Z = (X̄ - μ) / (σ / √n)")
        print("where:")
        print("X̄ = sample mean")
        print("μ = population mean")
        print("σ = population standard deviation")
        print("n = sample size")


# Key Assumptions
class KeyAssumptions:
    def __init__(self):
        pass

    def describe_key_assumptions(self):
        print("Key Assumptions for CLT:")
        print("1. Random Sampling: The sample must be chosen randomly.")
        print("2. Independence: Each data point should be independent.")
        print("3. Large Enough Sample Size: A sample size of at least 30 is usually enough.")
        print("4. Finite Mean and Variance: The population should have a defined average and variation.")


# Practical Applications
class PracticalApplications:
    def __init__(self):
        pass

    def describe_practical_applications(self):
        print("Practical Applications of CLT:")
        print("1. Model Evaluation and Confidence Intervals")
        print("2. A/B Testing")
        print("3. Error and Uncertainty Estimation")
        print("4. Bootstrapping")
        print("5. Feature Importance")


# Example of CLT
class ExampleOfCLT:
    def __init__(self):
        import numpy as np
        self.population = np.random.exponential(scale=2.0, size=100000)

    def simulate_clt(self):
        import matplotlib.pyplot as plt
        sample_size = 50
        num_samples = 1000
        sample_means = []

        for _ in range(num_samples):
            sample = np.random.choice(self.population, size=sample_size)
            sample_means.append(np.mean(sample))

        plt.hist(sample_means, bins=40, color='skyblue', edgecolor='black')
        plt.title('Sampling Distribution of Web Page Load Time (Means)')
        plt.xlabel('Sample Mean Load Time')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()


def main():
    print("Central Limit Theorem")
    introduction = Introduction()
    introduction.describe_clt()

    clt_formula = CLTFormula()
    clt_formula.describe_clt_formula()

    key_assumptions = KeyAssumptions()
    key_assumptions.describe_key_assumptions()

    practical_applications = PracticalApplications()
    practical_applications.describe_practical_applications()

    example_of_clt = ExampleOfCLT()
    example_of_clt.simulate_clt()


if __name__ == "__main__":
    main()