import pandas as pd
import numpy as np

# 1. Load the dataset
df = pd.read_csv('data/raw/online_sales_dataset.csv')

# 2. Convert InvoiceDate to datetime objects for time-series analysis
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# 3. Standardize Categorical Data
# Fix common typo in PaymentMethod
df['PaymentMethod'] = df['PaymentMethod'].replace('paypall', 'PayPal')

# 4. Handle Logical Errors (Negative Values)
# Quantity and UnitPrice should be positive for sales analysis. 
# Negative values often represent returns or data entry errors.
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# 5. Handle Missing Values
# Fill missing CustomerID with -1 to represent 'Guest' or 'Unknown'
df['CustomerID'] = df['CustomerID'].fillna(-1).astype(int)

# Fill missing ShippingCost with the median cost
df['ShippingCost'] = df['ShippingCost'].fillna(df['ShippingCost'].median())

# Fill missing WarehouseLocation with 'Unknown'
df['WarehouseLocation'] = df['WarehouseLocation'].fillna('Unknown')

# 6. Handle Outliers in Discounts
# Ensure discount values don't exceed 1.0 (100%)
df.loc[df['Discount'] > 1.0, 'Discount'] = 1.0

# 7. Remove Duplicate Rows
df = df.drop_duplicates()

# 8. Save the cleaned dataset
df.to_csv('online_sales_cleaned.csv', index=False)
df.to_excel('data/cleaned/online_sales_cleaned.xlsx', index=False)

print("Data cleaning complete. Cleaned file saved as 'online_sales_cleaned.csv'.")
print("Data cleaning complete. Cleaned file saved as 'online_sales_cleaned.xlsx'.")
print(df.info())