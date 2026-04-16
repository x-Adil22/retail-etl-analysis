psql -U postgres -d retail_db

CREATE TABLE retail_data (
    invoice_no TEXT,
    stock_code TEXT,
    description TEXT,
    quantity INT,
    invoice_date TIMESTAMP,
    unit_price FLOAT,
    customer_id FLOAT,
    country TEXT,
    revenue FLOAT,
    month TEXT
);

\copy retail_data FROM 'C:\\Users\\Dell\\Desktop\\E_Commerce_ETL_Project\\CSV\\retail_data.csv' DELIMITER ',' CSV HEADER; # Adjust the file path as needed

SELECT * FROM retail_data LIMIT 10;    # Display the first 10 rows to verify data loading

SELECT COUNT(*) FROM retail_data;      # Check the total number of records loaded into the table

