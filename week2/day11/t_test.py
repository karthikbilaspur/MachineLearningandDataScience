# t_test.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_t_test(self):
        print("The T-test is used to compare the averages of two groups to see if they are significantly different from each other.")
        print("It's a part of hypothesis testing where we start with the assumption (null hypothesis) that the two group means are the same.")
        print("Then the test helps you decide if there's enough evidence to reject that assumption and conclude that the groups are different.")


# One Sample T-test
class OneSampleTTest:
    def __init__(self):
        pass

    def describe_one_sample_t_test(self):
        print("A one-sample T-test is used to compare the mean of a sample to a known population mean.")
        print("Example: The weights of 25 obese people were taken before enrolling them into a nutrition camp.")
        print("The population mean weight is 45 kg. After finishing the camp, the sample mean was 75 with a standard deviation of 25.")

    def calculate_t_score(self, sample_mean: float, population_mean: float, sample_std: float, sample_size: int) -> float:
        t_score = (sample_mean - population_mean) / (sample_std / sample_size ** 0.5)
        return t_score


# Independent Sample T-test
class IndependentSampleTTest:
    def __init__(self):
        pass

    def describe_independent_sample_t_test(self):
        print("An independent sample T-test is used to compare the means of two independent samples.")
        print("Example: Researchers want to see if two teaching methods, A and B, produce different exam scores.")
        print("Samples for both methods are collected independently.")

    def calculate_t_score(self, sample1_mean: float, sample2_mean: float, sample1_std: float, sample2_std: float, sample1_size: int, sample2_size: int) -> float:
        t_score = (sample1_mean - sample2_mean) / ((sample1_std ** 2 / sample1_size) + (sample2_std ** 2 / sample2_size)) ** 0.5
        return t_score


# Paired Two-sample T-test
class PairedTwoSampleTTest:
    def __init__(self):
        pass

    def describe_paired_two_sample_t_test(self):
        print("A paired two-sample T-test is used to compare the means of two related samples.")
        print("Example: Scores (out of 25) of the subjects Math1 and Math2 are taken for a sample of 10 students.")

    def calculate_t_score(self, sample1: list, sample2: list) -> float:
        import numpy as np
        from scipy import stats
        t_score, _ = stats.ttest_rel(sample1, sample2)
        return t_score


def main():
    print("T-test")
    introduction = Introduction()
    introduction.describe_t_test()

    one_sample_t_test = OneSampleTTest()
    one_sample_t_test.describe_one_sample_t_test()
    t_score = one_sample_t_test.calculate_t_score(75, 45, 25, 25)
    print("T-score:", t_score)

    independent_sample_t_test = IndependentSampleTTest()
    independent_sample_t_test.describe_independent_sample_t_test()
    t_score = independent_sample_t_test.calculate_t_score(78, 82, 10, 12, 20, 20)
    print("T-score:", t_score)

    paired_two_sample_t_test = PairedTwoSampleTTest()
    paired_two_sample_t_test.describe_paired_two_sample_t_test()
    sample1 = [4, 4, 7, 16, 20, 11, 13, 9, 11, 15]
    sample2 = [15, 16, 14, 14, 22, 22, 23, 18, 18, 19]
    t_score = paired_two_sample_t_test.calculate_t_score(sample1, sample2)
    print("T-score:", t_score)


if __name__ == "__main__":
    main()