# Import necessary libraries
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from tabulate import tabulate

def load_data():
    """
    Load 20newsgroups dataset
    """
    newsgroups = fetch_20newsgroups(subset='all', categories=['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.gun', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc'])
    return newsgroups.data, newsgroups.target

def preprocess_data(data, target):
    """
    Preprocess data by creating a bag-of-words representation
    """
    vectorizer = CountVectorizer(binary=True)
    X = vectorizer.fit_transform(data)
    y = target
    return X, y

def split_data(X, y):
    """
    Split data into training and testing sets
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Train a Bernoulli Naive Bayes model
    """
    bnb = BernoulliNB()
    bnb.fit(X_train, y_train)
    return bnb

def evaluate_model(bnb, X_test, y_test):
    """
    Evaluate the model using accuracy score, classification report, and confusion matrix
    """
    y_pred = bnb.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

def explain_bnb():
    """
    Explain how Bernoulli Naive Bayes works
    """
    print("\nHow Bernoulli Naive Bayes Works:")
    print("-----------------------------------")
    print("1. Assumption: The features are binary (0/1).")
    print("2. Calculate Parameters: Calculate the parameters (theta) for each feature in each class.")
    print("3. Calculate Likelihood: Calculate the likelihood of each feature given the class using the Bernoulli distribution.")
    print("   P(x|y) = theta^x * (1-theta)^(1-x)")
    print("4. Calculate Posterior: Calculate the posterior probability of each class given the features using Bayes' theorem.")
    print("   P(y|x) = P(x|y) * P(y) / P(x)")
    print("5. Predict: Predict the class with the highest posterior probability.")
    print("   y_pred = argmax(P(y|x))")

def compare_bnb_mnb_gnb():
    """
    Compare Bernoulli Naive Bayes, Multinomial Naive Bayes, and Gaussian Naive Bayes
    """
    table = [
        ["Bernoulli Naive Bayes", "Multinomial Naive Bayes", "Gaussian Naive Bayes"],
        ["Designed for binary features", "Designed for discrete features", "Suitable for continuous features"],
        ["Assumes binary features (0/1)", "Assumes features and represent its counts like word counts", "Assumes a Gaussian distribution for the likelihood"],
        ["Commonly used in text classification tasks", "Commonly used in NLP for document classification tasks", "Commonly used in tasks involving continuous data such as medical diagnosis, fraud detection and weather prediction"],
        ["Likelihood calculated using the Bernoulli distribution", "Likelihood calculated using the multinomial distribution", "Likelihood modeled using the Gaussian distribution"],
        ["Efficient when features are binary", "Efficient when the number of features is very high like in text datasets with thousands of words", "Can handle continuous data but if the data is sparse or contains many outliers it struggle with accuracy"]
    ]
    print("\nComparison of Bernoulli Naive Bayes, Multinomial Naive Bayes, and Gaussian Naive Bayes:")
    print(tabulate(table, headers="firstrow", tablefmt="grid"))

def main():
    data, target = load_data()
    X, y = preprocess_data(data, target)
    X_train, X_test, y_train, y_test = split_data(X, y)
    bnb = train_model(X_train, y_train)
    evaluate_model(bnb, X_test, y_test)
    explain_bnb()
    compare_bnb_mnb_gnb()

if __name__ == "__main__":
    main()