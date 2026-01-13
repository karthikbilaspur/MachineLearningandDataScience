# 🔥 Machine learning (ML) is like teaching a computer to learn from data and make predictions or decisions 😎.

# What is Machine Learning?
# ML is a subset of AI that uses algorithms to identify patterns in data and make predictions or decisions without being explicitly programmed.

# Real-life Applications:
# 1. Image recognition (e.g., self-driving cars, facial recognition)
# 2. Recommendation systems (e.g., Netflix, Amazon)
# 3. Natural language processing (e.g., chatbots, language translation)
# 4. Predictive analytics (e.g., credit risk, disease diagnosis)

# Types of Machine Learning:
# 1. Supervised Learning: Labeled data, e.g., spam vs. not spam emails
# 2. Unsupervised Learning: Unlabeled data, e.g., customer segmentation
# 3. Reinforcement Learning: Trial and error, e.g., game playing

# Let's use Python to demonstrate a simple supervised learning example using scikit-learn:

# Import necessary libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def main():
    # Load iris dataset
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a logistic regression model
    model = LogisticRegression(max_iter=1000)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    main()