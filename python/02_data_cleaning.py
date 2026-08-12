import pandas as pd

# Load dataset
df = pd.read_csv("../dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# -------------------------------
# Basic Information
# -------------------------------
print("Dataset Shape Before Cleaning:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# -------------------------------
# Clean TotalCharges Column
# -------------------------------

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Fill missing values with median
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

# -------------------------------
# Check again
# -------------------------------
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDataset Shape After Cleaning:", df.shape)

# -------------------------------
# Save Clean Dataset
# -------------------------------
df.to_csv("../dataset/cleaned_telco_churn.csv", index=False)

print("\nCleaned dataset saved successfully!")