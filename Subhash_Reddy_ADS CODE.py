
import pandas as pd
import matplotlib.pyplot as plt

def plot_monthly_sales_over_years(file_path):
    
    df_sales = pd.read_csv(file_path, encoding='ISO-8859-1', index_col=0)

    # Convert 'ORDERDATE' to datetime format
    df_sales['ORDERDATE'] = pd.to_datetime(df_sales['ORDERDATE'])

    # Assuming 'sales' is your DataFrame
    data = df_sales.groupby(['YEAR_ID', 'MONTH_ID']).sum(numeric_only=True).reset_index()

    # Create the line plot using Matplotlib
    plt.figure(figsize=(10, 6))

    # Loop through unique YEAR_ID values and plot lines
    for year in data['YEAR_ID'].unique():
        year_data = data[data['YEAR_ID'] == year]
        plt.plot(year_data['MONTH_ID'], year_data['SALES'], label=f'Year {year}', marker='o')

    # Customize labels and title
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Monthly Sales Over Years')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_sales_histogram(file_path):
    
    df_sales = pd.read_csv(file_path, encoding='ISO-8859-1', index_col=0)

    # Plot histogram for 'SALES' column
    plt.figure(figsize=(10, 6))
    plt.hist(df_sales['SALES'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Sales')
    plt.ylabel('Frequency')
    plt.title('Histogram of Sales')
    plt.grid(True)
    plt.show()

def plot_total_sales_per_quarter(file_path):
    
    df_sales = pd.read_csv(file_path, encoding='ISO-8859-1', index_col=0)

    # Assuming 'sales' is your DataFrame
    data = df_sales.groupby(['YEAR_ID', 'QTR_ID'])['SALES'].sum().reset_index()

    # Create the bar plot using Matplotlib
    plt.figure(figsize=(10, 6))

    # Loop through unique YEAR_ID values and plot bars
    for year in data['YEAR_ID'].unique():
        year_data = data[data['YEAR_ID'] == year]
        plt.bar(year_data['QTR_ID'], year_data['SALES'], label=f'Year {year}')

    # Customize labels and title
    plt.xlabel('Quarter')
    plt.ylabel('Sales')
    plt.title('Total Sales Per Quarter')
    plt.legend()
    plt.grid(axis='y')

    plt.show()

# Specify the file path to your CSV file
file_path = r'sales_data_sample.csv'

# Call each function with the file path
plot_monthly_sales_over_years(file_path)
plot_sales_histogram(file_path)
plot_total_sales_per_quarter(file_path)
