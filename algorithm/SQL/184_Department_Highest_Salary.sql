# Write your MySQL query statement below
SELECT
    d.Name AS 'Department'
    ,e.Name AS 'Employee'
    ,e.Salary
FROM Employee e
JOIN Department d
    ON e.DepartmentId = d.Id
WHERE
    (SELECT COUNT(DISTINCT e2.Salary)
    FROM
        Employee e2
    WHERE
        e2.Salary > e.Salary
            AND e.DepartmentId = e2.DepartmentId
            ) < 3

# Write your MySQL query statement below
SELECT 
    d.Name AS 'Department'
    ,e.Name AS 'Employee'
    ,e.Salary
FROM Employee AS e
JOIN Department AS d
ON e.DepartmentId = d.Id
WHERE
    (SELECT COUNT(DISTINCT e2.Salary)
    FROM
        Employee e2
    WHERE
        e2.Salary > e.Salary
            AND e.DepartmentId = e2.DepartmentId
            ) < 1;

SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
    )
;

-- BAD: Error 42000: Column 'a.Employee' is invalid in the select list because it is not contained in either an aggregate function or the GROUP BY clause (8120)
-- SELECT 
--     a.Department
--     ,a.Employee
--     ,MAX(a.Salary) AS Salary
-- FROM
-- (SELECT 
--     d.Name AS 'Department'
--     ,e.Name AS 'Employee'
--     ,e.Salary
-- FROM Employee AS e
-- JOIN Department AS d
-- ON e.DepartmentId = d.Id) AS a
-- GROUP BY Department;

