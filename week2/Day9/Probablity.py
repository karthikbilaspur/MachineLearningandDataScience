# probability_in_data_science.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_importance(self):
        print("Probability is a fundamental concept in data science that helps us understand and quantify uncertainty in data.")
        print("It is a crucial tool for making informed decisions and predictions in the presence of uncertainty.")
        print("Probability is used in various aspects of data science, including data analysis, modeling, and visualization.")


# Probability
class Probability:
    def __init__(self):
        pass

    def describe_probability(self):
        print("Probability:")
        print("1. Definition:")
        print("   - Probability is a measure of the likelihood of an event occurring.")
        print("   - It is a number between 0 and 1 that represents the probability of an event.")
        print("2. Interpretation:")
        print("   - A probability of 0 indicates that an event is impossible.")
        print("   - A probability of 1 indicates that an event is certain.")
        print("   - A probability between 0 and 1 indicates the likelihood of an event occurring.")


# Types of Probability
class TypesOfProbability:
    def __init__(self):
        pass

    def describe_types(self):
        print("Types of Probability:")
        print("1. Classical Probability:")
        print("   - Classical probability is based on the assumption that all outcomes are equally likely.")
        print("   - It is calculated as the number of favorable outcomes divided by the total number of outcomes.")
        print("2. Empirical Probability:")
        print("   - Empirical probability is based on observed data.")
        print("   - It is calculated as the number of times an event occurs divided by the total number of trials.")
        print("3. Subjective Probability:")
        print("   - Subjective probability is based on personal judgment or opinion.")
        print("   - It is often used in situations where there is limited data or uncertainty.")


# Applications of Probability in Data Science
class ApplicationsOfProbabilityInDataScience:
    def __init__(self):
        pass

    def describe_applications(self):
        print("Applications of Probability in Data Science:")
        print("1. Data Analysis:")
        print("   - Probability is used in data analysis to understand and summarize data.")
        print("   - It helps us identify patterns and trends in data.")
        print("2. Modeling:")
        print("   - Probability is used in modeling to make predictions and forecasts.")
        print("   - It helps us quantify uncertainty and make informed decisions.")
        print("3. Hypothesis Testing:")
        print("   - Probability is used in hypothesis testing to determine the significance of results.")
        print("   - It helps us make informed decisions about accepting or rejecting hypotheses.")


# Example of Probability in Data Science
class ExampleOfProbabilityInDataScience:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def calculate_probability(self):
        import numpy as np
        mean = np.mean(self.data)
        std_dev = np.std(self.data)
        probability = np.exp(-((3 - mean) ** 2) / (2 * std_dev ** 2)) / (std_dev * np.sqrt(2 * np.pi))
        print("Probability:")
        print(f"P(X=3) = {probability}")


def main():
    print("Probability in Data Science")
    introduction = Introduction()
    introduction.describe_importance()

    probability = Probability()
    probability.describe_probability()

    types_of_probability = TypesOfProbability()
    types_of_probability.describe_types()

    applications_of_probability_in_data_science = ApplicationsOfProbabilityInDataScience()
    applications_of_probability_in_data_science.describe_applications()

    example_of_probability_in_data_science = ExampleOfProbabilityInDataScience()
    example_of_probability_in_data_science.calculate_probability()


if __name__ == "__main__":
    main()