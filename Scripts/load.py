import pandas as pd 
from sqlalchemy import create_engine

def load_data(df):

    engine = create_engine("postgresql://aimlock@localhost:5432/retail_db") # Create a connection to the PostgreSQL database
    df.to_sql("retail_data", engine, if_exists = 'fail',index=False) # Load the cleaned data into the "retail_data" table in the database, if the table already exists, it will raise an error (if_exists='fail') and it will not include the index column (index=False)

if __name__ == "__main__":
    df = pd.read_csv("/Users/aimlock/Desktop/python/E_Commerce_ETL_Project/Dataset/Processed/cleaned_data.csv") # Read the cleaned data from a CSV file
    load_data(df)

