# non_linear_svm.py

"""
Non-Linear SVM
===============

Introduction
------------

Non-Linear SVM is an extension of Linear SVM that can handle complex, non-linearly separable data using kernels.

Kernel Functions
----------------

1. **Radial Basis Function (RBF)**: Captures patterns in data by measuring the distance between points.
2. **Polynomial Kernel**: Models more complex relationships using polynomial equations.
3. **Sigmoid Kernel**: Mimics neural network behavior using sigmoid function.

Examples
--------

### Example 1: Non-Linear SVM with RBF Kernel

Classify concentric circles dataset using RBF kernel.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Create and split dataset
X, y = make_circles(n_samples=500, factor=0.5, noise=0.05, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Non-Linear SVM with RBF kernel
svm_rbf = SVC(kernel='rbf', C=1, gamma=0.5)
svm_rbf.fit(X_train, y_train)

# Evaluate model
y_pred = svm_rbf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy (RBF): {accuracy:.2f}")
print("Classification Report (RBF):\n", classification_report(y_test, y_pred))
print("Confusion Matrix (RBF):\n", confusion_matrix(y_test, y_pred))

# Visualize decision boundary
def plot_decision_boundary(X, y, model, title):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.Paired)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', cmap=plt.cm.Paired)
    plt.title(title)
    plt.show()

plot_decision_boundary(X, y, svm_rbf, "Non-Linear SVM with RBF Kernel")


"""
### Example 2: Non-Linear SVM with Polynomial Kernel

Classify two moons dataset using polynomial kernel.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Create and split dataset
X, y = make_moons(n_samples=500, noise=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Non-Linear SVM with polynomial kernel
svm_poly = SVC(kernel='poly', degree=3, C=1, coef0=1)
svm_poly.fit(X_train, y_train)

# Evaluate model
y_pred = svm_poly.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy (Poly): {accuracy:.2f}")
print("Classification Report (Poly):\n", classification_report(y_test, y_pred))
print("Confusion Matrix (Poly):\n", confusion_matrix(y_test, y_pred))

plot_decision_boundary(X, y, svm_poly, "Non-Linear SVM with Polynomial Kernel")


"""
### Comparison of Kernels

Compare performance of different kernels on concentric circles dataset.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create and split dataset
X, y = make_circles(n_samples=500, factor=0.5, noise=0.05, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

kernels = ['linear', 'rbf', 'poly']
accuracies = []

for kernel in kernels:
    svm = SVC(kernel=kernel, C=1)
    svm.fit(X_train, y_train)
    y_pred = svm.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)
    print(f"Accuracy ({kernel}): {accuracy:.2f}")

plt.bar(kernels, accuracies)
plt.xlabel("Kernel")
plt.ylabel("Accuracy")
plt.title("Comparison of Kernels")
plt.show()