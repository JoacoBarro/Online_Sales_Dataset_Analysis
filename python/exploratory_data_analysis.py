import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv('data/cleaned/online_sales_cleaned.csv')

# 2. Preprocessing & Feature Engineering
# Convert InvoiceDate to datetime objects
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create financial columns
df['GrossRevenue'] = df['Quantity'] * df['UnitPrice']
df['DiscountAmount'] = df['GrossRevenue'] * df['Discount']
df['NetRevenue'] = df['GrossRevenue'] - df['DiscountAmount']
df['TotalOrderValue'] = df['NetRevenue'] + df['ShippingCost']

# Create time-based columns for analysis
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['YearMonth'] = df['InvoiceDate'].dt.to_period('M').astype(str)

# Save the enhanced dataset to a new CSV file
df.to_csv('data/cleaned/online_sales_enhanced.csv', index=False)
df.to_excel('data/cleaned/online_sales_enhanced.xlsx', index=False)

# 3. Exploratory Data Analysis (Visualizations)
sns.set_theme(style="whitegrid")

# Visualization 1: Monthly Sales Trend
plt.figure(figsize=(12, 6))
monthly_sales = df.groupby('YearMonth')['TotalOrderValue'].sum().reset_index()
sns.lineplot(data=monthly_sales, x='YearMonth', y='TotalOrderValue', marker='o')
plt.xticks(rotation=45)
plt.title('Monthly Total Sales Trend (2020-2025)')
plt.xlabel('Month')
plt.ylabel('Total Sales Value ($)')
plt.tight_layout()
plt.savefig('python/graphs/sales_trend.png')

# Visualization 2: Total Sales by Category
plt.figure(figsize=(10, 6))
cat_revenue = df.groupby('Category')['TotalOrderValue'].sum().sort_values(ascending=False).reset_index()
sns.barplot(data=cat_revenue, x='TotalOrderValue', y='Category', palette='viridis')
plt.title('Total Sales by Product Category')
plt.xlabel('Total Sales Value ($)')
plt.tight_layout()
plt.savefig('python/graphs/category_revenue.png')

# Visualization 3: Correlation Heatmap of Numerical Features
plt.figure(figsize=(10, 8))
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('python/graphs/correlation_matrix.png')

# Visualization 4: Order Priority Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='OrderPriority', palette='Set2', order=['Low', 'Medium', 'High'])
plt.title('Distribution of Order Priority')
plt.tight_layout()
plt.savefig('python/graphs/order_priority.png')

# Visualization 5: Top 10 Countries by Revenue
plt.figure(figsize=(10, 6))
country_revenue = df.groupby('Country')['TotalOrderValue'].sum().nlargest(10).reset_index()
sns.barplot(data=country_revenue, x='TotalOrderValue', y='Country', palette='magma')
plt.title('Top 10 Countries by Total Sales')
plt.xlabel('Total Sales Value ($)')
plt.tight_layout()
plt.savefig('python/graphs/top_countries.png')

# Visualization 6: Order Return Status (Pie Chart)
plt.figure(figsize=(7, 7))
returns = df['ReturnStatus'].value_counts()
plt.pie(returns, labels=returns.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#99ff99'])
plt.title('Order Return Status Distribution')
plt.tight_layout()
plt.savefig('python/graphs/return_status.png')

# 4. Summary Statistics
print("--- Data Summary Statistics ---")
print(df.describe())
