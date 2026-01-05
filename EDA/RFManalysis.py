
# rfm_analysis.py

import pandas as pd

# === Step 1: Load your cleaned dataset () ===
# Make sure this path matches your actual cleaned dataset file
file_path = "/Users/vini/Downloads/farfetch hackathon data/fashion_sales.xlsm"
df_products = pd.read_excel(file_path, sheet_name="Product_Master")   # or CSV if you saved it

print("✅ Dataset loaded:", df_products.shape)
print(df_products.head())

# === Step 2: Recency calculation ===
# New season FW25 = most recent (1), else 0
df_products['Recency'] = df_products['Details'].apply(lambda x: 1 if 'New Season' in str(x) else 0)

# === Step 3: Frequency calculation ===
# Count number of SKUs per Brand
frequency = df_products.groupby('Brand')['Product_ID'].count().reset_index()
frequency.rename(columns={'Product_ID': 'Frequency'}, inplace=True)
