-- my solution
# Write your MySQL query statement below
SELECT Id AS id, cap_m AS month, SUM(Salary) AS Salary
FROM
(
    SELECT e.Id, e.Month AS cap_m, e2.Month AS iter_m, e2.Salary FROM 
        Employee AS e,
        Employee AS e2,
        (
            SELECT Id, MAX(MONTH) AS rct_m
            FROM Employee
            GROUP BY 1
        ) AS a
        WHERE 
            e.Id = a.Id
            AND e.Month < a.rct_m
            AND e2.Id = e.Id
            AND e2.Month BETWEEN e.Month - 2 AND e.Month
) AS x
GROUP BY 1, 2
ORDER BY 1 ASC, 2 DESC;

SELECT
    E1.id,
    E1.month,
    (IFNULL(E1.salary, 0) + IFNULL(E2.salary, 0) + IFNULL(E3.salary, 0)) AS Salary
FROM
    Employee E1
        LEFT JOIN
    Employee E2 ON (E2.id = E1.id
        AND E2.month = E1.month - 1)
        LEFT JOIN
    Employee E3 ON (E3.id = E1.id
        AND E3.month = E1.month - 2)
ORDER BY E1.id ASC , E1.month DESC
;

-- exclude most recent month (silly)
SELECT
    E1.id,
    E1.month,
    (IFNULL(E1.salary, 0) + IFNULL(E2.salary, 0) + IFNULL(E3.salary, 0)) AS Salary
FROM
    (SELECT
        id, MAX(month) AS month
    FROM
        Employee
    GROUP BY id
    HAVING COUNT(*) > 1) AS maxmonth
        LEFT JOIN
    Employee E1 ON (maxmonth.id = E1.id
        AND maxmonth.month > E1.month)
        LEFT JOIN
    Employee E2 ON (E2.id = E1.id
        AND E2.month = E1.month - 1)
        LEFT JOIN
    Employee E3 ON (E3.id = E1.id
        AND E3.month = E1.month - 2)
ORDER BY id ASC , month DESC;