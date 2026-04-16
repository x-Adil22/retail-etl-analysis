from extract import extract_data
from transform import transform_data
from load import load_data

df = extract_data("/Users/aimlock/Desktop/python/E_Commerce_ETL_Project/Dataset/raw/Online_Retail_Data_Set.csv")
df_clean = transform_data(df)
load_data(df_clean)
