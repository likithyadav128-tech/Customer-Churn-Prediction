import pandas as pd
import joblib
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ---------------------------------------
# Load Processed Dataset
# ---------------------------------------

X_train = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\Customer_Churn_Prediction\dataset\X_train.csv")
X_test = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\Customer_Churn_Prediction\dataset\X_test.csv")

y_train = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\Customer_Churn_Prediction\dataset\y_train.csv").squeeze()

y_test = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\Customer_Churn_Prediction\dataset\y_test.csv").squeeze()

print("Processed datasets loaded successfully!")

# ---------------------------------------
# Train Model
# ---------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# ---------------------------------------
# Prediction
# ---------------------------------------

y_pred = model.predict(X_test)

# ---------------------------------------
# Accuracy
# ---------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy :", round(accuracy*100,2), "%")

# ---------------------------------------
# Confusion Matrix
# ---------------------------------------

print("\nConfusion Matrix")

print(confusion_matrix(y_test, y_pred))

# ---------------------------------------
# Classification Report
# ---------------------------------------

print("\nClassification Report\n")

print(classification_report(y_test, y_pred))

# ---------------------------------------
# Save Model
# ---------------------------------------

os.makedirs(r"C:\Users\likit\OneDrive\Documents\Customer_Churn_Prediction\models", exist_ok=True)

joblib.dump(
    model,
    r"C:\Users\likit\OneDrive\Documents\Customer_Churn_Prediction\models\churn_prediction_model.pkl"
)

print("\nModel Saved Successfully!")

print("\nLocation:")
print(r"C:\Users\likit\OneDrive\Documents\Customer_Churn_Prediction\models\churn_prediction_model.pkl")