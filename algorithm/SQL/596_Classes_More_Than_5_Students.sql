# Write your MySQL query statement below
SELECT a.class FROM (
    SELECT class, COUNT(DISTINCT student) AS cnt 
    FROM courses 
    GROUP BY class
    HAVING cnt >= 5
) AS a;

# Write your MySQL query statement below
SELECT class
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;