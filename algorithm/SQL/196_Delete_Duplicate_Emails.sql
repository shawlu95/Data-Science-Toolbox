# Write your MySQL query statement below
-- Mysql won't make copy for the original table even with alias p1 so just as other language you cannot update the table when you are using data inside this table as conditions.
DELETE FROM Person WHERE Id IN (
    SELECT Id FROM (
        SELECT p1.Id
        FROM Person p1, Person p2
        WHERE p1.Email = p2.Email and p1.Id > p2.Id
    ) AS tmp);

DELETE
From Person
WHERE Id NOT IN (SELECT * FROM
                    (SELECT MIN(p1.Id)
                    FROM Person p1
                    GROUP BY p1.Email) 
                 AS tmp);
                
Delete p1  
    FROM Person p1, Person p2
    WHERE p1.Email = p2.Email and p1.Id > p2.Id