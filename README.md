# 📊 Online Sales Dataset Analysis

An end-to-end **data analytics project** built using the Online Sales Dataset from Kaggle.
This repository showcases the full analytics workflow: **data cleaning, feature engineering, exploratory data analysis (EDA), and executive-level dashboards built in Tableau.**

The project is designed as a **portfolio-ready business case**, focused on extracting actionable insights from real-world sales data.

## 🎯 Project Objectives

• Clean and prepare raw transactional sales data  

• Engineer business-relevant metrics for analysis  

• Perform exploratory data analysis using Python  

• Create professional Tableau dashboards for decision-making  

• Present insights across sales, logistics, and customer behavior  

## 📌 Dataset Information

• **Name**: Online Sales Dataset  

• **Source**: Kaggle  

• **Author**: Yusuf Delikkaya  

• **Link**: https://www.kaggle.com/datasets/yusufdelikkaya/online-sales-dataset  

The dataset contains online retail transaction records, including product details, pricing, discounts, shipping costs, customer behavior, and order status across multiple countries and years.

## 🧼 Data Cleaning

**Script**: *python/data_cleaning.py*

### **Main steps**:

  • Converted date fields to datetime format  

  • Fixed categorical inconsistencies (e.g. payment methods)  

  • Removed invalid records (negative quantity or unit price)  

  • Handled missing values (customers, shipping cost, warehouse)  

  • Capped discount values at logical limits  

  • Removed duplicate rows  

### **Outputs**:

  • *online_sales_cleaned.csv*

  • *online_sales_cleaned.xlsx*

## 🧠 Feature Engineering & Exploratory Data Analysis

###  **Script**: *python/exploratory_data_analysis.py*

  • Engineered Metrics  

  • Gross Revenue  

  • Discount Amount  

  • Net Revenue  

  • Total Order Value  

  • Time features (Year, Month, YearMonth)  

  • EDA Visualizations  

  • Monthly sales trends  

  • Revenue by product category  

  • Correlation matrix of numerical variables  

  • Order priority distribution  

  • Top countries by revenue  

  • Return status distribution  

All generated visuals are saved in *python/graphs/.*

### **Outputs**:

  • *online_sales_enhanced.csv*

  • *online_sales_enhanced.xlsx*

## 📈 Tableau Dashboards

### The Tableau dashboards are structured to support **executive and operational decision-making**, covering:

  • Executive Sales Overview  

  • Business Performance Analysis  

  • Customer & Channel Insights  

  • Logistics & Operations  

### Key KPIs include:

• Net Revenue

• Quantity Sold

• Return Rate

• Average Discount

• Shipping Cost Ratio

### Dashboards are available both as:

• Tableau workbook (.twb)

• Exported PDFs for easy sharing

## 🛠️ Tools & Technologies

• **Python** (pandas, numpy, matplotlib, seaborn)

• **Tableau**

• **Excel**

• **Git & GitHub**

## ▶️ How to Run the Project

1.Clone the repository:  
> git clone https://github.com/yourusername/online-sales-dataset-analysis.git

2.Install dependencies:  
> pip install pandas numpy matplotlib seaborn

3-Run data cleaning:  
> python python/data_cleaning.py

4.Run EDA and feature engineering:  
> python python/exploratory_data_analysis.py

5.Open the Tableau workbook:  
> tableau/workbook/business_performance_analysis.twb

## 📌 Notes

• This project is intended for **portfolio and educational purposes**

• The analysis emphasizes **business KPIs and decision support**

• The structure allows easy extension into forecasting, segmentation, or machine learning models

## 👤 Author

**Joaquín Barro**  
Information Systems Engineering Student at Universidad Nacional del Sur (Argentina).  
Aspiring Data Analyst / Business Intelligence Analyst.    
Skilled in Python, SQL, Tableau, and end-to-end analytics projects.
