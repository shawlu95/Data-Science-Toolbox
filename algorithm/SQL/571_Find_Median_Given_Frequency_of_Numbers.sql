# Write your MySQL query statement below
SELECT 
    AVG(Number) as median
FROM 
    (
        SELECT 
            Number, 
            @cum_freq AS lb, 
            (@cum_freq:=@cum_freq + Frequency) AS ub
        FROM Numbers, (SELECT @cum_freq:=0) init
        ORDER BY Number
    ) AS T1,
     (
        SELECT 
            SUM(Frequency) AS total_freq
        FROM Numbers
     ) AS T2
WHERE lb <= (total_freq/2) 
    AND ub >= (total_freq/2)