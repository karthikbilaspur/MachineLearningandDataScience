# data_science_concepts.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_importance(self):
        print("In data science, we often work with samples instead of entire populations.")
        print("The Central Limit Theorem (CLT) helps us assume normality in sample means,")
        print("while Hypothesis Testing helps us make decisions based on those samples.")


# Skewness in Data Science
class SkewnessInDataScience:
    def __init__(self):
        pass

    def describe_skewness(self):
        print("Skewness tells us whether the data is symmetric or tilted to one side.")
        print("Understanding skewness is important before applying statistical methods that assume normality.")
        print("Example: Income Distribution")
        print("Suppose a company's employee salaries are: [25k, 28k, 30k, 32k, 35k, 36k, 100k]")
        print("Most salaries are around 25k–36k, but one outlier (100k) pulls the average to the right.")
        print("This is a positively skewed distribution. The mean will be higher than the median due to the high-income outlier.")


# Central Limit Theorem (CLT) in Data Science
class CLTInDataScience:
    def __init__(self):
        pass

    def describe_clt(self):
        print("The Central Limit Theorem says that if we take many large samples and find their averages,")
        print("those averages form a normal distribution even if the original data is skewed.")
        print("This allows data scientists to use normal distribution formulas to calculate confidence intervals and error margins,")
        print("even when the raw data is not normal.")
        print("Example: Estimating Average Daily Orders")
        print("A delivery company wants to estimate the average daily orders without checking the full month’s data.")
        print("Data (10 days): [100, 200, ..., 700], Population Mean = 360")
        print("Sample Means: 262.5, 412.5, 425")
        print("Avg. of Sample Means = 366.7 (close to 360)")
        print("This shows how the Central Limit Theorem helps small samples give a reliable estimate of the overall mean.")


# Hypothesis Testing in Data Science
class HypothesisTestingInDataScience:
    def __init__(self):
        pass

    def describe_hypothesis_testing(self):
        print("Hypothesis testing checks if a sample result is statistically different from a known or expected value.")
        print("It helps in deciding whether to reject the null hypothesis based on a threshold called the significance level (commonly 0.05).")
        print("Example: Has the Complaint Rate Decreased?")
        print("A company claims its new packaging reduced complaints. Earlier, 10% of orders had complaints.")
        print("In a recent sample of 1000 orders, only 70 complaints were reported.")
        print("H₀: Complaint rate = 10%")
        print("H₁: Complaint rate < 10%")
        print("Sample rate = 0.07")
        print("z ≈ –3.16, Critical z = –1.645")
        print("Since –3.16 < –1.645, we reject H₀ there’s strong evidence the complaint rate has dropped.")


def main():
    print("Use of Skewness, Central Limit Theorem and Hypothesis Testing in Data Science")
    introduction = Introduction()
    introduction.describe_importance()

    skewness_in_data_science = SkewnessInDataScience()
    skewness_in_data_science.describe_skewness()

    clt_in_data_science = CLTInDataScience()
    clt_in_data_science.describe_clt()

    hypothesis_testing_in_data_science = HypothesisTestingInDataScience()
    hypothesis_testing_in_data_science.describe_hypothesis_testing()


if __name__ == "__main__":
    main()