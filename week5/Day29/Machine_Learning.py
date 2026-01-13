# machine_learning_types.py

# Supervised Learning
"""
Supervised learning is a type of machine learning where the model is trained on labeled data.
The goal is to learn a mapping between input data and the corresponding output labels.

Types of Supervised Learning:
1. **Regression**: Predicting a continuous output value (e.g., house prices, stock prices)
2. **Classification**: Predicting a categorical output label (e.g., spam vs. not spam emails, cancer vs. no cancer)

Advantages:
- **High Accuracy**: Supervised learning models can achieve high accuracy when trained on large, high-quality datasets.
- **Well-defined Evaluation Metrics**: Supervised learning models can be evaluated using well-defined metrics (e.g., accuracy, precision, recall).
- **Wide Range of Applications**: Supervised learning is applicable to a wide range of problems, including image classification, natural language processing, and recommender systems.

Disadvantages:
- **Requires Labeled Data**: Supervised learning requires large amounts of labeled data, which can be time-consuming and expensive to obtain.
- **Prone to Overfitting**: Supervised learning models can be prone to overfitting, especially when the model is complex and the dataset is small.
- **Limited Ability to Handle New Data**: Supervised learning models may not perform well on new, unseen data that is different from the training data.

Examples:
- Linear Regression
- Logistic Regression
- Decision Trees
- Random Forest
- Support Vector Machines (SVMs)
"""

# Unsupervised Learning
"""
Unsupervised learning is a type of machine learning where the model is trained on unlabeled data.
The goal is to discover patterns, relationships, or groupings in the data.

Types of Unsupervised Learning:
1. **Clustering**: Grouping similar data points into clusters (e.g., customer segmentation)
2. **Dimensionality Reduction**: Reducing the number of features in the data while preserving important information (e.g., PCA, t-SNE)
3. **Anomaly Detection**: Identifying data points that don't fit the normal pattern (e.g., fraud detection)

Advantages:
- **No Need for Labeled Data**: Unsupervised learning can be applied to unlabeled data, which is often abundant and inexpensive to obtain.
- **Ability to Discover Hidden Patterns**: Unsupervised learning can discover hidden patterns and relationships in the data.
- **Flexibility**: Unsupervised learning can be used for a variety of tasks, including data exploration and preprocessing.

Disadvantages:
- **Difficult to Evaluate**: Unsupervised learning models can be difficult to evaluate, as there is no clear metric for success.
- **Sensitive to Hyperparameters**: Unsupervised learning models can be sensitive to hyperparameters, which can affect the quality of the results.
- **May Not Provide Clear Insights**: Unsupervised learning models may not provide clear insights or actionable recommendations.

Examples:
- K-Means Clustering
- Hierarchical Clustering
- Principal Component Analysis (PCA)
- t-Distributed Stochastic Neighbor Embedding (t-SNE)
- One-class SVM
"""

# Comparison of Supervised and Unsupervised Learning
"""
| **Characteristics** | **Supervised Learning** | **Unsupervised Learning** |
| --- | --- | --- |
| **Data** | Labeled data | Unlabeled data |
| **Goal** | Learn a mapping between input and output | Discover patterns and relationships |
| **Types** | Regression, Classification | Clustering, Dimensionality Reduction, Anomaly Detection |
| **Advantages** | High accuracy, well-defined evaluation metrics, wide range of applications | No need for labeled data, ability to discover hidden patterns, flexibility |
| **Disadvantages** | Requires labeled data, prone to overfitting, limited ability to handle new data | Difficult to evaluate, sensitive to hyperparameters, may not provide clear insights |
| **Examples** | Linear Regression, Logistic Regression, Decision Trees | K-Means Clustering, PCA, t-SNE |
"""

# Example Code
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# Supervised Learning Example (Linear Regression)
def supervised_learning_example():
    # Load dataset
    X, y = datasets.load_diabetes(return_X_y=True)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)
    print("Predictions:", predictions)

# Unsupervised Learning Example (K-Means Clustering)
def unsupervised_learning_example():
    # Load dataset
    X, _ = datasets.load_iris(return_X_y=True)

    # Train model
    model = KMeans(n_clusters=3)
    model.fit(X)

    # Get cluster labels
    labels = model.labels_
    print("Cluster Labels:", labels)

if __name__ == "__main__":
    supervised_learning_example()
    unsupervised_learning_example()