/* Write your T-SQL query statement below */
SELECT c.Name AS 'Customers'
FROM Customers AS c
WHERE c.Id NOT IN (SELECT CustomerId FROM Orders);