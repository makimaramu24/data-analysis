import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load dataset
data = pd.read_csv('customers-100.csv')
print("✅ Dataset loaded!")
print(data.head())

# Step 2: Basic exploration
print("\n📊 Dataset info:")
print(data.info())

print("\n🧮 Missing values per column:")
missing_counts = data.isnull().sum()
print(missing_counts)

print("\n📈 Summary statistics:")
print(data.describe())

# Step 3: Visualize missing values as a figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(missing_counts.index, missing_counts.values, color='steelblue')
ax.set_title('Missing Values per Column', fontsize=16)
ax.set_xlabel('Columns', fontsize=12)
ax.set_ylabel('Missing Count', fontsize=12)
plt.xticks(rotation=45, ha='right')
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Step 4: Handle missing values
for col in data.columns:
    if data[col].isnull().sum() > 0:
        if data[col].dtype == 'object':
            data[col].fillna(data[col].mode()[0], inplace=True)
        else:
            data[col].fillna(data[col].median(), inplace=True)
print("\n✅ Missing values filled.")

# Step 5: Encode categorical variables manually
categorical_cols = data.select_dtypes(include=['object']).columns
data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)
print("✅ Categorical variables encoded with one-hot encoding.")
print(data.head())

# Step 6: Scale numerical features manually
numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns
for col in numerical_cols:
    mean = data[col].mean()
    std = data[col].std()
    data[col] = (data[col] - mean) / std
p
