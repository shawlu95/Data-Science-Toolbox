/* Write your T-SQL query statement below */

SELECT
    e.Name AS 'Employee'
FROM
    Employee AS e
LEFT JOIN
    Employee as m
ON e.ManagerId = m.Id
WHERE e.Salary > m.Salary;