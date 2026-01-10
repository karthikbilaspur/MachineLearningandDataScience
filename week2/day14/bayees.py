# bayes_theorem.py

import numpy as np

def bayes_theorem(prior_disease, sensitivity, false_positive_rate, specificity):
    """
    Apply Bayes' Theorem to calculate the probability of disease given a positive test result.

    Parameters:
    prior_disease (float): Prior probability of disease (P(Disease))
    sensitivity (float): Probability of positive test given disease (P(+|Disease))
    false_positive_rate (float): Probability of positive test given no disease (P(+|No Disease))
    specificity (float): Probability of negative test given no disease (P(-|No Disease))

    Returns:
    float: Posterior probability of disease given a positive test result (P(Disease|+))
    """
    # Calculate P(No Disease)
    prior_no_disease = 1 - prior_disease
    
    # Calculate P(+|No Disease)
    false_positive = 1 - specificity
    
    # Calculate P(+)
    p_positive = (sensitivity * prior_disease) + (false_positive * prior_no_disease)
    
    # Apply Bayes' Theorem
    posterior_disease = (sensitivity * prior_disease) / p_positive
    
    return posterior_disease

def main():
    # Given probabilities
    prior_disease = 0.05  # 5% of population has the disease
    sensitivity = 0.95  # 95% chance of positive test if disease is present
    false_positive_rate = 0.10  # 10% chance of positive test if disease is not present
    specificity = 1 - false_positive_rate  # 90% chance of negative test if disease is not present

    # Calculate posterior probability
    posterior_probability = bayes_theorem(prior_disease, sensitivity, false_positive_rate, specificity)
    
    print(f"Posterior probability of disease given a positive test result: {posterior_probability:.2%}")

if __name__ == "__main__":
    main()