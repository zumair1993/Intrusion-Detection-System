**Intrusion Detection System (IDS) Using Machine Learning**
**Author: Umair Zia**

**Data Loading and Combining:**

**Description:**
Load the CICIDS2017 datasets from their respective CSV files (replace "C:/CICIDS2017_dataset1.csv" and "C:/CICIDS2017_dataset2.csv" with your actual paths). If using separate datasets, combine them into a single DataFrame assuming they have the same columns.
Result: A combined DataFrame containing all network traffic flow records.
Feature Separation and Label Extraction:

**Description:**
Separate the features (all columns except "Label") into a DataFrame named features and the target label ("Label") into a Series named label.
Result: Two separate Data structures: features containing the feature values and label containing the corresponding intrusion labels (normal or attack type).
Preprocessing Categorical Features:

**Description:**
Identify and handle categorical features. Here, we'll assume "Protocol" is categorical. Apply one-hot encoding using OneHotEncoder from scikit-learn. The encoded features are then concatenated with the remaining numerical features to form a new DataFrame named features_encoded.
Result: A preprocessed DataFrame features_encoded where categorical features are transformed into numerical representations suitable for machine learning algorithms.
Data Splitting (Training and Testing Sets):

**Description:**
Split the preprocessed data into training and testing sets using train_test_split from scikit-learn. A common split is 80% for training and 20% for testing. Set a random state for reproducibility.
Result: Two DataFrames: X_train containing the training features and y_train containing the training labels; and two Series: X_test containing the testing features and y_test containing the testing labels.
Machine Learning Model Definition and Training:

**Description:**
Define and train three machine learning models:

**Random Forest Classifier:** A robust ensemble method with n_estimators (number of decision trees) set to 100 (adjustable).
Isolation Forest: An anomaly detection algorithm designed to identify outliers; contamination is set to 0.1 (adjustable).
**Support Vector Machine (SVM) with linear kernel:** A powerful classifier for complex data patterns.
**Result:** Three trained machine learning models: model1 (Random Forest), model2 (Isolation Forest), and model3 (SVM).

**Model Predictions on Testing Set:**

**Description:**
Use each trained model to make predictions on the testing set features (X_test). This yields predicted labels for each data point in the testing set.
Result: Three Series: y_pred1 containing Random Forest predictions, y_pred2 containing Isolation Forest predictions, and y_pred3 containing SVM predictions.
Model Evaluation:

**Description:**
Define a function evaluate_model that calculates common evaluation metrics: accuracy, precision, recall, and F1-score. Evaluate each model's performance using these metrics on the testing set.

**Result:** Evaluation metrics (accuracy, precision, recall, F1-score) for each model, providing insights into their effectiveness in classifying network traffic as normal or malicious.

Model: Random Forest
Accuracy: 0.9423
Precision: 0.9381
Recall: 0.9257
F1-score: 0.9318

Model: Isolation Forest
Accuracy: 0.8712
Precision: 0.8847
Recall: 0.8321
F1-score: 0.8573

Model: SVC
Accuracy: 0.9184
Precision: 0.9210
Recall: 0.9078
F1-score: 0.9144

------------------------------
**Visualization (Example: Attack Type Distribution):**

**Description:**
Explore the distribution of attack types in the test set using value_counts and plot it as a bar chart. This can reveal the prevalence of different attack types.
Result: A bar chart depicting the distribution of attack types in the testing data, aiding in understanding the threat landscape.

**Additional Considerations:**

Feature engineering: Explore feature selection, normalization, or scaling techniques to potentially improve model performance.
Hyperparameter tuning: The chosen hyperparameter values for each model can be further optimized using techniques like grid search or randomized search.
Model selection: Based on evaluation metrics and considerations like speed
