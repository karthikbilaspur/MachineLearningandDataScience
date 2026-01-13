# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve, auc
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as imbpipeline

# Load the dataset
disease_df = pd.read_csv("framingham.csv")

# Drop irrelevant features and handle missing values
disease_df.drop(columns=['education'], inplace=True, axis=1)
disease_df.rename(columns={'male': 'Sex_male'}, inplace=True)
disease_df.dropna(axis=0, inplace=True)

# Explore the dataset
print("Dataset shape:", disease_df.shape)
print("Dataset columns:", disease_df.columns)
print("Dataset head:\n", disease_df.head())
print("Dataset info:\n", disease_df.info())
print("Dataset description:\n", disease_df.describe())

# Visualize the dataset
plt.figure(figsize=(10, 6))
sns.countplot(x='TenYearCHD', data=disease_df, palette="BuGn_r")
plt.title("TenYearCHD Distribution")
plt.show()

# Split the dataset into features and target
X = disease_df.drop('TenYearCHD', axis=1)
y = disease_df['TenYearCHD']

# Feature selection
selector = SelectKBest(mutual_info_classif, k=10)
X_selected = selector.fit_transform(X, y)

# Get the selected features
selected_features = X.columns[selector.support_]
print("Selected features:", selected_features)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.3, random_state=4)

# Handle class imbalance using SMOTE
smote = SMOTE(random_state=4)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Define the pipeline
pipeline = imbpipeline([
    ('scaler', StandardScaler()),
    ('logreg', LogisticRegression())
])

# Define the hyperparameters to tune
param_grid = {
    'logreg__C': [0.1, 1, 10],
    'logreg__penalty': ['l1', 'l2']
}

# Perform grid search
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='f1_macro')
grid_search.fit(X_train_res, y_train_res)

# Get the best model
best_model = grid_search.best_estimator_

# Make predictions
y_pred = best_model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, best_model.predict_proba(X_test)[:, 1]))

# Plot ROC curve
fpr, tpr, _ = roc_curve(y_test, best_model.predict_proba(X_test)[:, 1])
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

# Plot confusion matrix
cm = confusion_matrix(y_test, y_pred)
conf_matrix = pd.DataFrame(data=cm, columns=['Predicted:0', 'Predicted:1'], index=['Actual:0', 'Actual:1'])
plt.figure(figsize=(8, 5))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap="Greens")
plt.show()