# conditional_probability.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_importance(self):
        print("Conditional probability is a fundamental concept in probability theory that helps us understand the probability of an event occurring given that another event has occurred.")
        print("It is a crucial concept in statistics, machine learning, and decision-making under uncertainty.")
        print("Conditional probability is used in various fields, including medicine, finance, and engineering.")


# Conditional Probability
class ConditionalProbability:
    def __init__(self):
        pass

    def describe_conditional_probability(self):
        print("Conditional Probability:")
        print("1. Definition:")
        print("   - Conditional probability is the probability of an event A occurring given that event B has occurred.")
        print("   - It is denoted as P(A|B) and is calculated as P(A|B) = P(A ∩ B) / P(B)")
        print("   - where P(A ∩ B) is the probability of both events A and B occurring, and P(B) is the probability of event B occurring.")
        print("2. Interpretation:")
        print("   - P(A|B) represents the probability of event A occurring given that event B has occurred.")
        print("   - If P(A|B) = P(A), then events A and B are independent.")
        print("   - If P(A|B) ≠ P(A), then events A and B are dependent.")


# Types of Conditional Probability
class TypesOfConditionalProbability:
    def __init__(self):
        pass

    def describe_types(self):
        print("Types of Conditional Probability:")
        print("1. Joint Probability:")
        print("   - Joint probability is the probability of two or more events occurring together.")
        print("   - It is denoted as P(A ∩ B) and is calculated as P(A ∩ B) = P(A|B) * P(B)")
        print("2. Marginal Probability:")
        print("   - Marginal probability is the probability of an event occurring without considering other events.")
        print("   - It is denoted as P(A) and is calculated as P(A) = Σ P(A ∩ B)")
        print("3. Conditional Probability:")
        print("   - Conditional probability is the probability of an event occurring given that another event has occurred.")
        print("   - It is denoted as P(A|B) and is calculated as P(A|B) = P(A ∩ B) / P(B)")


# Uses of Conditional Probability
class UsesOfConditionalProbability:
    def __init__(self):
        pass

    def describe_uses(self):
        print("Uses of Conditional Probability:")
        print("1. Decision-Making:")
        print("   - Conditional probability is used in decision-making under uncertainty.")
        print("   - It helps us make informed decisions by considering the probability of different outcomes.")
        print("2. Machine Learning:")
        print("   - Conditional probability is used in machine learning algorithms such as Naive Bayes and Bayesian networks.")
        print("   - It helps us model complex relationships between variables.")
        print("3. Medical Diagnosis:")
        print("   - Conditional probability is used in medical diagnosis to determine the probability of a disease given symptoms.")
        print("   - It helps doctors make informed decisions about treatment options.")


# Example of Conditional Probability
class ExampleOfConditionalProbability:
    def __init__(self):
        self.p_a = 0.5
        self.p_b = 0.3
        self.p_a_and_b = 0.2

    def calculate_conditional_probability(self):
        p_a_given_b = self.p_a_and_b / self.p_b
        print("Conditional Probability:")
        print(f"P(A|B) = {p_a_given_b}")


def main():
    print("Conditional Probability")
    introduction = Introduction()
    introduction.describe_importance()

    conditional_probability = ConditionalProbability()
    conditional_probability.describe_conditional_probability()

    types_of_conditional_probability = TypesOfConditionalProbability()
    types_of_conditional_probability.describe_types()

    uses_of_conditional_probability = UsesOfConditionalProbability()
    uses_of_conditional_probability.describe_uses()

    example_of_conditional_probability = ExampleOfConditionalProbability()
    example_of_conditional_probability.calculate_conditional_probability()


if __name__ == "__main__":
    main()