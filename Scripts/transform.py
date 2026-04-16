import pandas as pd 

def transform_data(df):
    df = df.dropna(subset=['CustomerID']) # Drop rows with missing CustomerID

    df = df[df['Quanitity'] > 0] # Remove rows with non-positive quantity

    df = df.drop_duplicates() # Remove duplicate rows

    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])   # Convert InvoiceDate to datetime format

    df['Revenue'] = df['Quantity'] * df['UnitPrice'] # Calculate revenue for each transaction

    df['Month'] = df['InvoiceDate'].dt.to_period('M') # Extract month from InvoiceDate for monthly analysis

    customer_spend = df.groupby('CustomerID')['Revenue'].sum().reset_index() # Calculate total spend per customer
    customer_spend.rename(columns={'Revenue' : 'TotalSpend'}, inplace = True)

    order_count = df.groupby('CustomerID')['InvoiceNo'].nunique().reset_index() # Calculate number of orders per customer
    order_count.rename(columns={'InvoiceNo' : 'OrderCount'}, inplace=True)

    customer_feature = customer_spend.merge(order_count, on='CustomerID') # Merge total spend and order count into a single DataFrame

    return df

if __name__ == "__main__":
    df = pd.read_csv('/Users/aimlock/Desktop/python/E_Commerce_ETL_Project/Dataset/raw/Online_Retail_Data_Set.csv')
    df_clean = transform_data(df)
    print(df_clean.head())

    