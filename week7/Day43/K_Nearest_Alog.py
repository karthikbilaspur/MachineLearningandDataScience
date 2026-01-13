# Import necessary libraries
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import cross_val_score
import numpy as np

def main():
    # 1. Generating and Visualizing the 2D Data
    X, y = make_moons(n_samples=300, noise=0.3, random_state=42)
    df = pd.DataFrame(X, columns=["Feature 1", "Feature 2"])
    df['Target'] = y
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="Feature 1", y="Feature 2", hue="Target", palette="Set1")
    plt.title("2D Classification Data (make_moons)")
    plt.grid(True)
    plt.show()

    # 2. Train-Test Split and Normalization
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.3, random_state=42, stratify=y
    )

    # 3. Fit the k-NN Model and Evaluate
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print(f"Test Accuracy (k=5): {accuracy_score(y_test, y_pred):.2f}")

    # 4. Cross-Validation to Choose Best k
    k_range = range(1, 21)
    cv_scores = []
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn, X_scaled, y, cv=5, scoring='accuracy')
        cv_scores.append(scores.mean())
    plt.figure(figsize=(8, 5))
    plt.plot(k_range, cv_scores, marker='o')
    plt.title("k-NN Cross-Validation Accuracy vs k")
    plt.xlabel("Number of Neighbors: k")
    plt.ylabel("Cross-Validated Accuracy")
    plt.grid(True)
    plt.show()
    best_k = k_range[np.argmax(cv_scores)]
    print(f"Best k from cross-validation: {best_k}")

    # 5. Training with Best k
    best_knn = KNeighborsClassifier(n_neighbors=best_k)
    best_knn.fit(X_train, y_train)
    y_pred = best_knn.predict(X_test)

    # 6. Evaluate Using More Metrics
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Class 0", "Class 1"])
    disp.plot(cmap="Blues")
    plt.title(f"Confusion Matrix (k={best_k})")
    plt.grid(False)
    plt.show()
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=["Class 0", "Class 1"]))

    # 7. Visualize Decision Boundary with Best k
    x_min, x_max = X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1
    y_min, y_max = X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
    Z = best_knn.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.3)
    sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:, 1], hue=y, palette="Set1", edgecolor='k')
    plt.title(f"Decision Boundary with Best k = {best_k}")
    plt.xlabel("Feature 1 (scaled)")
    plt.ylabel("Feature 2 (scaled)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()