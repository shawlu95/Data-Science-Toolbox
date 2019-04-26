-- use correlated subquery (faster)
SELECT customer_number
FROM orders
GROUP BY customer_number 
ORDER BY COUNT(order_number) DESC
LIMIT 1;

-- slower, select twice
SELECT a.customer_number FROM (
    SELECT 
    	customer_number
    	, COUNT(order_number) AS order_cnt
    FROM orders 
    GROUP BY customer_number 
    ORDER BY order_cnt DESC) 
AS a LIMIT 1;