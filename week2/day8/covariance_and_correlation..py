# covariance_and_correlation.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_importance(self):
        print("Covariance and correlation are two important concepts in statistics that measure the relationship between two variables.")
        print("They help us understand how changes in one variable are associated with changes in another variable.")
        print("Covariance and correlation are used in various fields, including finance, economics, and social sciences.")


# Covariance
class Covariance:
    def __init__(self):
        pass

    def describe_covariance(self):
        print("Covariance:")
        print("1. Definition:")
        print("   - Covariance measures the average of the products of the deviations of two variables from their means.")
        print("   - It is a measure of the linear relationship between two variables.")
        print("2. Formula:")
        print("   - Cov(X, Y) = Σ[(xi - μx)(yi - μy)] / (n - 1)")
        print("   - where xi and yi are individual data points, μx and μy are the means of X and Y, and n is the number of data points.")
        print("3. Interpretation:")
        print("   - A positive covariance indicates that the variables tend to increase or decrease together.")
        print("   - A negative covariance indicates that the variables tend to move in opposite directions.")
        print("   - A zero covariance indicates that the variables are uncorrelated.")


# Correlation
class Correlation:
    def __init__(self):
        pass

    def describe_correlation(self):
        print("Correlation:")
        print("1. Definition:")
        print("   - Correlation measures the strength and direction of the linear relationship between two variables.")
        print("   - It is a standardized measure of covariance.")
        print("2. Formula:")
        print("   - ρ(X, Y) = Cov(X, Y) / (σx * σy)")
        print("     where ρ(X, Y) is the correlation coefficient, Cov(X, Y) is the covariance, and σx and σy are the standard deviations of X and Y.")
        print("3. Interpretation:")
        print("   - A correlation of 1 indicates a perfect positive linear relationship.")
        print("   - A correlation of -1 indicates a perfect negative linear relationship.")
        print("   - A correlation of 0 indicates no linear relationship.")


# Types of Correlation
class TypesOfCorrelation:
    def __init__(self):
        pass

    def describe_types(self):
        print("Types of Correlation:")
        print("1. Pearson Correlation:")
        print("   - Measures the linear relationship between two continuous variables.")
        print("2. Spearman Correlation:")
        print("   - Measures the rank-order relationship between two variables.")
        print("3. Kendall Correlation:")
        print("   - Measures the rank-order relationship between two variables.")


# Example of Covariance and Correlation
class ExampleOfCovarianceAndCorrelation:
    def __init__(self):
        self.x = [1, 2, 3, 4, 5]
        self.y = [2, 3, 5, 7, 11]

    def calculate_covariance_and_correlation(self):
        import numpy as np
        covariance = np.cov(self.x, self.y)[0, 1]
        correlation = np.corrcoef(self.x, self.y)[0, 1]

        print("Covariance and Correlation:")
        print(f"Covariance: {covariance}")
        print(f"Correlation: {correlation}")


def main():
    print("Covariance and Correlation")
    introduction = Introduction()
    introduction.describe_importance()

    covariance = Covariance()
    covariance.describe_covariance()

    correlation = Correlation()
    correlation.describe_correlation()

    types_of_correlation = TypesOfCorrelation()
    types_of_correlation.describe_types()

    example_of_covariance_and_correlation = ExampleOfCovarianceAndCorrelation()
    example_of_covariance_and_correlation.calculate_covariance_and_correlation()


if __name__ == "__main__":
    main()