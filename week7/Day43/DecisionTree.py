# Decision Boundaries for Binary Classification 😊

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification

# What are Decision Boundaries?
# A decision boundary is a hypersurface that separates the classes in a classification problem.

# Binary Classification
# In binary classification, the decision boundary is a line (or hyperplane) that separates the two classes.

# Voronoi Diagram
# A Voronoi diagram is a partitioning of a plane into regions based on the proximity to a set of points.
# Each point in the plane is assigned to the nearest point in the set.

# How to use Voronoi Diagram?
# Voronoi diagrams can be used to visualize the decision boundaries of a KNN classifier.

# KNN Decision Boundaries
# KNN defines decision boundaries based on the K nearest neighbors of a point.
# The decision boundary is the set of points that are equidistant to the K nearest neighbors of different classes.

def plot_decision_boundary(X, y, knn):
    # Plot the decision boundary
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.show()

# Generate a binary classification dataset
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_classes=2, random_state=42)

# Create a KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)

# Train the model
knn.fit(X, y)

# Plot the decision boundary
plot_decision_boundary(X, y, knn)

# Factors that affect KNN decision boundaries:
# * **K**: The number of nearest neighbors
# * **Distance metric**: The distance metric used to calculate the distance between points
# * **Data distribution**: The distribution of the data
# * **Noise**: The presence of noise in the data

# Example: Effect of K on decision boundaries
for k in [1, 3, 5, 10]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X, y)
    plt.figure()
    plot_decision_boundary(X, y, knn)
    plt.title(f"K={k}")
plt.show()