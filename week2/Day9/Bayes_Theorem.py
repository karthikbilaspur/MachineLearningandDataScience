# bayes_theorem.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_importance(self):
        print("Bayes' theorem is a fundamental concept in probability theory that helps us update our beliefs about a hypothesis based on new evidence.")
        print("It is a powerful tool for reasoning under uncertainty and is widely used in many fields, including science, engineering, and medicine.")
        print("Bayes' theorem is named after Thomas Bayes, an 18th-century Presbyterian minister and mathematician.")


# Bayes' Theorem
class BayesTheorem:
    def __init__(self):
        pass

    def describe_bayes_theorem(self):
        print("Bayes' Theorem:")
        print("1. Definition:")
        print("   - Bayes' theorem is a mathematical formula for updating the probability of a hypothesis based on new evidence.")
        print("   - It is denoted as P(H|E) = P(E|H) * P(H) / P(E)")
        print("   - where P(H|E) is the posterior probability of the hypothesis given the evidence,")
        print("     P(E|H) is the likelihood of the evidence given the hypothesis,")
        print("     P(H) is the prior probability of the hypothesis, and")
        print("     P(E) is the marginal probability of the evidence.")
        print("2. Interpretation:")
        print("   - Bayes' theorem updates our belief about a hypothesis based on new evidence.")
        print("   - The posterior probability P(H|E) represents our updated belief about the hypothesis given the evidence.")


# Applications of Bayes' Theorem
class ApplicationsOfBayesTheorem:
    def __init__(self):
        pass

    def describe_applications(self):
        print("Applications of Bayes' Theorem:")
        print("1. Medical Diagnosis:")
        print("   - Bayes' theorem is used in medical diagnosis to determine the probability of a disease given symptoms.")
        print("   - It helps doctors make informed decisions about treatment options.")
        print("2. Spam Filtering:")
        print("   - Bayes' theorem is used in spam filtering to determine the probability of an email being spam given its content.")
        print("   - It helps email providers filter out unwanted emails.")
        print("3. Machine Learning:")
        print("   - Bayes' theorem is used in machine learning algorithms such as Naive Bayes and Bayesian networks.")
        print("   - It helps us model complex relationships between variables.")


# Example of Bayes' Theorem
class ExampleOfBayesTheorem:
    def __init__(self):
        self.p_h = 0.01  # Prior probability of having the disease
        self.p_e_given_h = 0.9  # Likelihood of testing positive given the disease
        self.p_e = 0.02  # Marginal probability of testing positive

    def calculate_bayes_theorem(self):
        p_h_given_e = (self.p_e_given_h * self.p_h) / self.p_e
        print("Bayes' Theorem:")
        print(f"P(H|E) = {p_h_given_e}")


def main():
    print("Bayes' Theorem")
    introduction = Introduction()
    introduction.describe_importance()

    bayes_theorem = BayesTheorem()
    bayes_theorem.describe_bayes_theorem()

    applications_of_bayes_theorem = ApplicationsOfBayesTheorem()
    applications_of_bayes_theorem.describe_applications()

    example_of_bayes_theorem = ExampleOfBayesTheorem()
    example_of_bayes_theorem.calculate_bayes_theorem()


if __name__ == "__main__":
    main()