import pandas as pd

# Load the dataset
df = pd.read_csv("../dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())
