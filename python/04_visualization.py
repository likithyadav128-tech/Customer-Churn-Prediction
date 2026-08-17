import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("../dataset/cleaned_telco_churn.csv")

# Style
sns.set(style="whitegrid")

# -------------------------------
# 1. Churn Distribution
# -------------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="Churn", data=df)
plt.title("Customer Churn Distribution")
plt.savefig("../images/churn_distribution.png")
plt.show()

# -------------------------------
# 2. Gender Distribution
# -------------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="gender", data=df)
plt.title("Gender Distribution")
plt.savefig("../images/gender_distribution.png")
plt.show()

# -------------------------------
# 3. Contract Type
# -------------------------------
plt.figure(figsize=(7,4))
sns.countplot(x="Contract", data=df)
plt.title("Contract Type")
plt.xticks(rotation=15)
plt.savefig("../images/contract_type.png")
plt.show()

# -------------------------------
# 4. Monthly Charges Histogram
# -------------------------------
plt.figure(figsize=(7,4))
sns.histplot(df["MonthlyCharges"], bins=30)
plt.title("Monthly Charges Distribution")
plt.savefig("../images/monthly_charges.png")
plt.show()

# -------------------------------
# 5. Tenure Distribution
# -------------------------------
plt.figure(figsize=(7,4))
sns.histplot(df["tenure"], bins=30)
plt.title("Customer Tenure")
plt.savefig("../images/tenure_distribution.png")
plt.show()

# -------------------------------
# 6. Churn by Contract
# -------------------------------
plt.figure(figsize=(7,4))
sns.countplot(x="Contract", hue="Churn", data=df)
plt.title("Churn by Contract Type")
plt.xticks(rotation=15)
plt.savefig("../images/churn_by_contract.png")
plt.show()

print("All visualizations created successfully!")