# Import necessary libraries
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

class NaiveBayes:
    """
    A Naive Bayes classifier implementation from scratch.

    Attributes:
        classes (np.ndarray): Unique classes in the dataset.
        mean (np.ndarray): Mean of each feature for each class.
        variance (np.ndarray): Variance of each feature for each class.
        prior (np.ndarray): Prior probability of each class.
    """

    def __init__(self):
        """
        Initialize the Naive Bayes classifier.
        """
        self.classes = None
        self.mean = None
        self.variance = None
        self.prior = None

    def fit(self, X, y):
        """
        Fit the Naive Bayes classifier to the training data.

        Parameters:
            X (np.ndarray): Feature matrix.
            y (np.ndarray): Target vector.
        """
        # Get unique classes
        self.classes = np.unique(y)

        # Initialize mean, variance, and prior arrays
        self.mean = np.zeros((len(self.classes), X.shape[1]))
        self.variance = np.zeros((len(self.classes), X.shape[1]))
        self.prior = np.zeros(len(self.classes))

        # Calculate mean, variance, and prior for each class
        for idx, c in enumerate(self.classes):
            # Get samples belonging to class c
            X_c = X[y == c]

            # Calculate mean of each feature for class c
            self.mean[idx, :] = X_c.mean(axis=0)

            # Calculate variance of each feature for class c
            self.variance[idx, :] = X_c.var(axis=0)

            # Calculate prior probability of class c
            self.prior[idx] = X_c.shape[0] / float(X.shape[0])

    def predict(self, X):
        """
        Make predictions on the test data.

        Parameters:
            X (np.ndarray): Feature matrix.

        Returns:
            np.ndarray: Predicted target vector.
        """
        # Make predictions for each sample
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        """
        Make a prediction for a single sample.

        Parameters:
            x (np.ndarray): Feature vector.

        Returns:
            int: Predicted class label.
        """
        # Initialize posterior probabilities
        posteriors = []

        # Calculate posterior probability for each class
        for idx, _ in enumerate(self.classes):
            # Calculate log prior probability
            prior = np.log(self.prior[idx])

            # Calculate log likelihood
            likelihood = -0.5 * np.sum(np.log(2 * np.pi * self.variance[idx, :]))
            likelihood -= 0.5 * np.sum((x - self.mean[idx, :]) ** 2 / (self.variance[idx, :]))

            # Calculate log posterior probability
            posterior = prior + likelihood
            posteriors.append(posterior)

        # Return class with highest posterior probability
        return self.classes[np.argmax(posteriors)]

def main():
    # Load iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create Naive Bayes classifier
    nb = NaiveBayes()
    nb.fit(X_train, y_train)

    # Make predictions
    y_pred = nb.predict(X_test)

    # Evaluate accuracy
    accuracy = np.sum(y_test == y_pred) / float(y_test.shape[0])
    print("Accuracy:", accuracy)

if __name__ == "__main__":
    main()