-- 1. Revenue Trend
SELECT 
    DATE_TRUNC('month', invoice_date) AS month,
    SUM(revenue) AS total_revenue
FROM retail_data
GROUP BY month
ORDER BY month;

-- 2. Top 20% Customers

SELECT customer_id, SUM(revenue) AS total_spent
FROM retail_data
GROUP BY customer_id
ORDER BY total_spent DESC;

-- 3. Repeat vs One-time Customers
SELECT 
    customer_id,
    COUNT(DISTINCT invoice_no) AS total_orders
FROM retail_data
GROUP BY customer_id;

-- 4. Country-wise Performance
SELECT 
    country,
    SUM(revenue) AS total_revenue
FROM retail_data
GROUP BY country
ORDER BY total_revenue DESC;

-- 5. Product Performance
SELECT 
    description,
    SUM(quantity) AS total_sold,
    SUM(revenue) AS total_revenue
FROM retail_data
GROUP BY description
ORDER BY total_revenue DESC;
