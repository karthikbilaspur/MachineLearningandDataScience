# f1_score.py

"""
F1 Score in Machine Learning
=============================================

F1 Score is a performance metric used in machine learning to evaluate how well a classification model performs on a dataset especially when the classes are imbalanced meaning one class appears much more frequently than another.
"""

# Import necessary libraries
from sklearn.metrics import f1_score, confusion_matrix, classification_report
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# F1 Score
# ------------

# Definition: F1 Score combines precision and recall using the harmonic mean.
# Formula: `F1 Score = 2 * (Precision * Recall) / (Precision + Recall)`
# Interpretation: A high F1 score indicates that the model is good at predicting positive instances, with few false positives and false negatives.

def calculate_f1_score(y_true, y_pred):
    """
    Calculate F1 score.

    Args:
        y_true (list): True labels.
        y_pred (list): Predicted labels.

    Returns:
        float: F1 score.
    """
    f1 = f1_score(y_true, y_pred, average='macro')
    return f1

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
    y_true = [0, 1, 2, 2, 2, 2, 1, 0, 2, 1, 0]
    y_pred = [0, 0, 2, 2, 1, 2, 1, 0, 1, 2, 1]

    # Calculate F1 score
    f1 = calculate_f1_score(y_true, y_pred)
    print("F1 Score:", f1)

    # Plot confusion matrix
    plot_confusion_matrix(y_true, y_pred)

    # Print classification report
    print(classification_report(y_true, y_pred))

    # Calculate F1 score per class
    f1_per_class = f1_score(y_true, y_pred, average=None)
    print("F1 Score per class:", f1_per_class)

    # Calculate micro-average F1 score
    f1_micro = f1_score(y_true, y_pred, average='micro')
    print("Micro-average F1 Score:", f1_micro)

    # Calculate macro-average F1 score
    f1_macro = f1_score(y_true, y_pred, average='macro')
    print("Macro-average F1 Score:", f1_macro)

    # Calculate weighted-average F1 score
    f1_weighted = f1_score(y_true, y_pred, average='weighted')
    print("Weighted-average F1 Score:", f1_weighted)

if __name__ == "__main__":
    main()