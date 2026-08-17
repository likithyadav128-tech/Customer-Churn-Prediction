import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../dataset/cleaned_telco_churn.csv")

# -----------------------------
# Dataset Overview
# -----------------------------
print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# -----------------------------
# Statistical Summary
# -----------------------------
print("\nStatistical Summary:")
print(df.describe())

# -----------------------------
# Categorical Columns Summary
# -----------------------------
print("\nCategorical Summary:")
print(df.describe(include="all"))

# -----------------------------
# Churn Distribution
# -----------------------------
print("\nChurn Distribution:")
print(df["Churn"].value_counts())

print("\nChurn Percentage:")
print(df["Churn"].value_counts(normalize=True) * 100)

# -----------------------------
# Gender Distribution
# -----------------------------
print("\nGender Distribution:")
print(df["gender"].value_counts())

# -----------------------------
# Contract Type
# -----------------------------
print("\nContract Type:")
print(df["Contract"].value_counts())

# -----------------------------
# Internet Service
# -----------------------------
print("\nInternet Service:")
print(df["InternetService"].value_counts())

# -----------------------------
# Payment Method
# -----------------------------
print("\nPayment Method:")
print(df["PaymentMethod"].value_counts())

# -----------------------------
# Monthly Charges
# -----------------------------
print("\nAverage Monthly Charges:")
print(df["MonthlyCharges"].mean())

# -----------------------------
# Total Charges
# -----------------------------
print("\nAverage Total Charges:")
print(df["TotalCharges"].mean())

# -----------------------------
# Tenure
# -----------------------------
print("\nAverage Tenure:")
print(df["tenure"].mean())