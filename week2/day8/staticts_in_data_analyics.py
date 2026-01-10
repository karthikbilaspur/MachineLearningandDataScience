# statistics_in_data_analytics.py

# Introduction
class Introduction:
    def __init__(self):
        pass

    def describe_importance(self):
        print("Statistics is a crucial component of data analytics, providing methods to collect, analyze, and interpret data.")
        print("It helps data analysts to extract insights and meaningful patterns from data, making informed decisions possible.")


# Data Collection
class DataCollection:
    def __init__(self):
        pass

    def describe_data_collection(self):
        print("Statistics helps in collecting data by:")
        print("1. Designing surveys and experiments to gather relevant data.")
        print("  Example: A company conducts a survey to understand customer satisfaction with their product.")
        print("2. Identifying the right data sources and sampling techniques.")
        print("  Example: A researcher uses random sampling to select participants for a study.")


# Data Analysis
class DataAnalysis:
    def __init__(self):
        pass

    def describe_data_analysis(self):
        print("Statistics helps in analyzing data by:")
        print("1. Summarizing data using descriptive statistics (mean, median, mode, etc.).")
        print("  Example: A company calculates the average salary of its employees to understand the salary distribution.")
        print("2. Visualizing data to identify patterns and trends.")
        print("  Example: A data analyst creates a histogram to visualize the distribution of customer ages.")
        print("3. Inferring population parameters from sample data using inferential statistics.")
        print("  Example: A researcher uses a sample of 1000 customers to estimate the average income of all customers in the city.")


# Data Interpretation
class DataInterpretation:
    def __init__(self):
        pass

    def describe_data_interpretation(self):
        print("Statistics helps in interpreting data by:")
        print("1. Identifying correlations and relationships between variables.")
        print("  Example: A data analyst finds a strong correlation between customer satisfaction and product quality.")
        print("2. Testing hypotheses and making predictions.")
        print("  Example: A researcher tests the hypothesis that a new marketing campaign increases sales.")
        print("3. Estimating uncertainty and quantifying risks.")
        print("  Example: A company estimates the probability of a product failure based on historical data.")


# Business Applications
class BusinessApplications:
    def __init__(self):
        pass

    def describe_business_applications(self):
        print("Statistics is used in various business applications, including:")
        print("1. Market research and customer segmentation.")
        print("2. Quality control and process improvement.")
        print("3. Financial analysis and risk management.")
        print("4. Predictive modeling and forecasting.")


def main():
    print("Statistics in Data Analytics")
    introduction = Introduction()
    introduction.describe_importance()

    data_collection = DataCollection()
    data_collection.describe_data_collection()

    data_analysis = DataAnalysis()
    data_analysis.describe_data_analysis()

    data_interpretation = DataInterpretation()
    data_interpretation.describe_data_interpretation()

    business_applications = BusinessApplications()
    business_applications.describe_business_applications()


if __name__ == "__main__":
    main()
