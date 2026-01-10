# z_test.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_z_test(self):
        print("A Z-test is a type of hypothesis test that compares the sample's average to the population's average")
        print("and calculates the Z-score, telling us how much the sample average is different from the population average")
        print("by looking at how much the data normally varies.")


# One Sample Z-test
class OneSampleZTest:
    def __init__(self):
        pass

    def describe_one_sample_z_test(self):
        print("A one-sample Z-test is used to determine if the mean of a single sample is significantly different")
        print("from a known population mean.")
        print("Example: A company claims that their new smartphone has an average battery life of 12 hours.")
        print("A consumer group tests 100 phones and finds an average battery life of 11.8 hours with a known")
        print("population standard deviation of 0.5 hours.")

    def calculate_z_score(self, sample_mean: float, population_mean: float, population_std: float, sample_size: int) -> float:
        z_score = (sample_mean - population_mean) / (population_std / sample_size ** 0.5)
        return z_score


# Two Sample Z-test
class TwoSampleZTest:
    def __init__(self):
        pass

    def describe_two_sample_z_test(self):
        print("A two-sample Z-test is used to compare the means of two independent samples.")
        print("Example: There are two groups of students preparing for a competition: Group A and Group B.")
        print("Group A has studied offline classes, while Group B has studied online classes.")
        print("After the examination, the score of each student comes.")

    def calculate_z_score(self, sample1_mean: float, sample2_mean: float, population1_std: float, population2_std: float, sample1_size: int, sample2_size: int) -> float:
        z_score = (sample1_mean - sample2_mean) / ((population1_std ** 2 / sample1_size) + (population2_std ** 2 / sample2_size)) ** 0.5
        return z_score


def main():
    print("Z-test")
    introduction = Introduction()
    introduction.describe_z_test()

    one_sample_z_test = OneSampleZTest()
    one_sample_z_test.describe_one_sample_z_test()
    z_score = one_sample_z_test.calculate_z_score(11.8, 12, 0.5, 100)
    print("Z-score:", z_score)

    two_sample_z_test = TwoSampleZTest()
    two_sample_z_test.describe_two_sample_z_test()
    z_score = two_sample_z_test.calculate_z_score(75, 80, 10, 12, 50, 60)
    print("Z-score:", z_score)


if __name__ == "__main__":
    main()