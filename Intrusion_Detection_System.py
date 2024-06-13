# Author: Umair Zia
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

# Define data paths
dataset1_path = "C://CICIDS2017_dataset1.csv"
dataset2_path = "C://CICIDS2017_dataset2.csv"

# Load datasets
data1 = pd.read_csv(dataset1_path)
data2 = pd.read_csv(dataset2_path)

# Combine datasets (assuming they have the same columns)
data = pd.concat([data1, data2], ignore_index=True)

# Separate features (all columns except "Label") and label ("Label")
features = data.drop("Label", axis=1)
label = data["Label"]

# Identify categorical features (assuming "Protocol" is categorical)
categorical_features = ["Protocol"]

# One-hot encoding for categorical features
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(sparse=False)
features_encoded = pd.concat([features.drop(categorical_features, axis=1),
                             pd.DataFrame(encoder.fit_transform(features[categorical_features]))], axis=1)

# Split data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(features_encoded, label, test_size=0.2, random_state=42)

# Define and train machine learning models (adjust hyperparameters as needed)
model1 = RandomForestClassifier(n_estimators=100)
model2 = IsolationForest(contamination=0.1)
model3 = SVC(kernel='linear')  # Consider other kernels like 'rbf'

# Train models
model1.fit(X_train, y_train)
model2.fit(X_train, y_train)
model3.fit(X_train, y_train)

# Make predictions for each model
y_pred1 = model1.predict(X_test)
y_pred2 = model2.predict(X_test)
y_pred3 = model3.predict(X_test)

# Evaluate model performance
def evaluate_model(y_true, y_pred):
  accuracy = accuracy_score(y_true, y_pred)
  precision = precision_score(y_true, y_pred)
  recall = recall_score(y_true, y_pred)
  f1 = f1_score(y_true, y_pred)
  return accuracy, precision, recall, f1

# Print evaluation metrics for each model
models = ["Random Forest", "Isolation Forest", "SVC"]
for i in range(3):
  model_name = models[i]
  y_pred = [y_pred1, y_pred2, y_pred3][i]
  accuracy, precision, recall, f1 = evaluate_model(y_test, y_pred)
  print(f"Model: {model_name}")
  print(f"Accuracy: {accuracy:.4f}")
  print(f"Precision: {precision:.4f}")
  print(f"Recall: {recall:.4f}")
  print(f"F1-score: {f1:.4f}")
  print("-" * 30)

# Example visualization: distribution of attack types in the test set
attack_types = y_test.value_counts().sort_values(ascending=False)
plt.bar(attack_types.index, attack_types.values)
plt.xlabel("Attack Type")
plt.ylabel("Number of Instances")
plt.title("Distribution of Attack Types in Test Set")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
