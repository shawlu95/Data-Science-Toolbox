

SELECT
    IFNULL(
        (
            SELECT Salary 
            FROM Employee 
            ORDER BY Salary DESC 
            LIMIT 1 OFFSET 1
        )
        , NULL
    )
AS SecondHighestSalary;