import pandas as pd
from sklearn.model_selection import train_test_split

# ---------------------------------
# Load Cleaned Dataset
# ---------------------------------
df = pd.read_csv(r"C:\Users\likit\OneDrive\Documents\Customer_Churn_Prediction\dataset\cleaned_telco_churn.csv")

print("Dataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

# ---------------------------------
# Remove Customer ID
# ---------------------------------
if "customerID" in df.columns:
    df.drop("customerID", axis=1, inplace=True)

# ---------------------------------
# Convert TotalCharges to Numeric
# ---------------------------------
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

# ---------------------------------
# Encode Target Variable
# ---------------------------------
df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})

# ---------------------------------
# Separate Features and Target
# ---------------------------------
X = df.drop("Churn", axis=1)
y = df["Churn"]

# ---------------------------------
# One-Hot Encode Categorical Columns
# ---------------------------------
X = pd.get_dummies(X, drop_first=True)

print("\nAfter Encoding")
print(X.head())

print("\nData Types")
print(X.dtypes)

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

# ---------------------------------
# Split Dataset
# ---------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# ---------------------------------
# Save Processed Data
# ---------------------------------
X_train.to_csv(r"C:\Users\likit\OneDrive\Documents\Customer_Churn_Prediction\dataset\X_train.csv", index=False)
X_test.to_csv(r"C:\Users\likit\OneDrive\Documents\Customer_Churn_Prediction\dataset\X_test.csv", index=False)
y_train.to_csv(r"C:\Users\likit\OneDrive\Documents\Customer_Churn_Prediction\dataset\y_train.csv", index=False)
y_test.to_csv(r"C:\Users\likit\OneDrive\Documents\Customer_Churn_Prediction\dataset\y_test.csv", index=False)

print("\nProcessed datasets saved successfully!")
print("Preprocessing Completed Successfully!")