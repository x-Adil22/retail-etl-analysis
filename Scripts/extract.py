import pandas as pd 

def extract_data(file_path):
    df = pd.read_csv(file_path)
    return df 

if __name__ == "__main__":
    df = extract_data("/Users/aimlock/Desktop/python/E_Commerce_ETL_Project/Dataset/raw/Online_Retail_Data_Set.csv")
    print(df.head(10))
    