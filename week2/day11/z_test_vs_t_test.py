# z_test_vs_t_test.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_z_test_vs_t_test(self):
        print("Z-tests are used when the population variance is known and the sample size is large,")
        print("while T-tests are used when the population variance is unknown and the sample size is small.")
        print("Here's a summary of the key differences:")

        print("\n| **Aspect** | **T-Test** | **Z-Test** |")
        print("| --- | --- | --- |")
        print("| **Purpose** | Compare means of small samples (n < 30) | Compare means of large samples (n ≥ 30) |")
        print("| **Assumptions** | Normally distributed data, approximate normality | Normally distributed data, known population standard deviation |")
        print("| **Population Standard Deviation** | Unknown | Known |")
        print("| **Sample Size** | Small (n < 30) | Large (n ≥ 30) |")
        print("| **Test Statistic** | T-distribution | Standard normal distribution (Z-distribution) |")
        print("| **Degrees of Freedom** | n1 + n2 - 2 | Not applicable |")
        print("| **Use Case** | Small sample analysis, comparing means between groups | Large sample analysis, population mean comparisons |")


# Z-Test
class ZTest:
    def __init__(self):
        pass

    def describe_z_test(self):
        print("A Z-test is used to compare the mean of a sample to a known population mean.")
        print("Example: Delivery Time Analysis")
        print("Suppose the company claims average delivery takes 2 days.")
        print("You check a sample of 50 deliveries that averaged 1.8 days, with a known population standard deviation of 0.5.")

    def calculate_z_score(self, sample_mean: float, population_mean: float, population_std: float, sample_size: int) -> float:
        z_score = (sample_mean - population_mean) / (population_std / sample_size ** 0.5)
        return z_score

    def interpret_z_score(self, z_score: float):
        if abs(z_score) > 1.96:
            print("Reject the null hypothesis. The sample mean is significantly different from the population mean.")
        else:
            print("Fail to reject the null hypothesis. The sample mean is not significantly different from the population mean.")


# T-Test
class TTest:
    def __init__(self):
        pass

    def describe_t_test(self):
        print("A T-test is used to compare the mean of a sample to a known population mean.")
        print("Example: Website Load Time")
        print("You want to test if a new version of a website loads faster.")
        print("You test it on 10 users and get:")
        print("Sample mean = 2.1s")
        print("Old mean = 2.5s")
        print("Sample SD = 0.3s")

    def calculate_t_score(self, sample_mean: float, population_mean: float, sample_std: float, sample_size: int) -> float:
        t_score = (sample_mean - population_mean) / (sample_std / sample_size ** 0.5)
        return t_score

    def interpret_t_score(self, t_score: float, degrees_of_freedom: int):
        from scipy.stats import t
        critical_t = t.ppf(0.975, degrees_of_freedom)
        if abs(t_score) > critical_t:
            print("Reject the null hypothesis. The sample mean is significantly different from the population mean.")
        else:
            print("Fail to reject the null hypothesis. The sample mean is not significantly different from the population mean.")


def main():
    print("Z-Test vs T-Test")
    introduction = Introduction()
    introduction.describe_z_test_vs_t_test()

    z_test = ZTest()
    z_test.describe_z_test()
    z_score = z_test.calculate_z_score(1.8, 2, 0.5, 50)
    print("Z-score:", z_score)
    z_test.interpret_z_score(z_score)

    t_test = TTest()
    t_test.describe_t_test()
    t_score = t_test.calculate_t_score(2.1, 2.5, 0.3, 10)
    print("T-score:", t_score)
    t_test.interpret_t_score(t_score, 9)


if __name__ == "__main__":
    main()