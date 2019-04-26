# Write your MySQL query statement below
SELECT 
    d.dept_name
    ,COUNT(s.student_id) AS student_number
FROM 
    student AS s
RIGHT JOIN
    department AS d
ON s.dept_id = d.dept_id
GROUP BY dept_name
ORDER BY student_number DESC, dept_name;

SELECT 
	d.dept_name
	,COUNT(s.student_id) AS student_number 
FROM
    department d LEFT JOIN student s
    ON d.dept_id = s.dept_id
GROUP BY 1
ORDER BY 2 DESC, 1;

-- output
-- {"headers":["dept_name","student_number"],"values":[["Engineering",2],["Science",1],["Law",0]]}

# Write your MySQL query statement below
SELECT 
    d.dept_name
    ,COUNT(s.student_id) AS student_number
FROM 
    student AS s
JOIN
    department AS d
ON s.dept_id = d.dept_id
GROUP BY dept_name
ORDER BY student_number DESC, dept_name;
-- output (same for inner join)
-- {"headers":["dept_name","student_number"],"values":[["Engineering",2],["Science",1]]}

# Write your MySQL query statement below
SELECT 
    d.dept_name
    ,COUNT(s.student_id) AS student_number
FROM 
    student AS s
LEFT JOIN
    department AS d
ON s.dept_id = d.dept_id
GROUP BY dept_name
ORDER BY student_number DESC, dept_name;
-- output
-- {"headers":["dept_name","student_number"],"values":[["Engineering",2],["Science",1]]}