# precision_recall.py

"""
Precision and Recall in Machine Learning
=============================================

Precision and recall are two fundamental metrics used to evaluate the performance of a classification model in machine learning.
"""

# Import necessary libraries
from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

# Precision
# ------------

# Definition: Precision measures the proportion of true positives (correctly predicted instances) among all positive predictions made by the model.
# Formula: `Precision = TP / (TP + FP)`
# Interpretation: A high precision indicates that the model is good at predicting positive instances, with few false positives.

# Recall
# ---------

# Definition: Recall measures the proportion of true positives among all actual positive instances in the dataset.
# Formula: `Recall = TP / (TP + FN)`
# Interpretation: A high recall indicates that the model is good at detecting all positive instances, with few false negatives.

# Advantages and Uses
# -----------------------

# Precision

# Advantages:
#     * Helps minimize false positives
#     * Useful when the cost of a false positive is high
# Real-life uses:
#     * Spam email detection: High precision ensures that legitimate emails are not incorrectly classified as spam.
#     * Medical diagnosis: High precision is crucial when diagnosing a disease to avoid unnecessary treatment or anxiety.

# Recall

# Advantages:
#     * Helps detect all positive instances
#     * Useful when the cost of a false negative is high
# Real-life uses:
#     * Disease screening: High recall is essential to detect all potential cases, even if it means some false positives.
#     * Credit card fraud detection: High recall helps detect all fraudulent transactions, even if it means investigating some legitimate transactions.

def calculate_precision_recall(y_true, y_pred):
    """
    Calculate precision and recall scores.

    Args:
        y_true (list): True labels.
        y_pred (list): Predicted labels.

    Returns:
        tuple: Precision and recall scores.
    """
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    return precision, recall

def plot_confusion_matrix(y_true, y_pred):
    """
    Plot confusion matrix.

    Args:
        y_true (list): True labels.
        y_pred (list): Predicted labels.
    """
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='g')
    plt.ylabel('Actual', fontsize=13)
    plt.title('Confusion Matrix', fontsize=17, pad=20)
    plt.gca().xaxis.set_label_position('top') 
    plt.xlabel('Prediction', fontsize=13)
    plt.gca().xaxis.tick_top()
    plt.show()

def main():
    # Example data
    y_true = [1, 1, 0, 1, 0, 0, 1, 1, 0]
    y_pred = [1, 1, 1, 0, 0, 0, 1, 1, 1]

    # Calculate precision and recall
    precision, recall = calculate_precision_recall(y_true, y_pred)
    print("Precision:", precision)
    print("Recall:", recall)

    # Plot confusion matrix
    plot_confusion_matrix(y_true, y_pred)

    # Print classification report
    print(classification_report(y_true, y_pred))

if __name__ == "__main__":
    main()