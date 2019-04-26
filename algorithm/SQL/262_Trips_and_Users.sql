-- exclude banned clients only
SELECT 
    Request_at AS Day, 
    ROUND(
        SUM(
            CASE 
                WHEN Status = 'completed' THEN 0
                ELSE 1
            END
        ) / COUNT(*), 2) AS 'Cancellation Rate'
FROM (
    SELECT t.* 
    FROM 
    Trips AS t
    LEFT JOIN
    Users AS u
        ON t.Client_Id = u.Users_Id
    WHERE u.Banned = 'No'
        AND Request_at BETWEEN '2013-10-01' AND '2013-10-03'
) AS c
GROUP BY Request_at
ORDER BY 1;

-- exclude both banned clients and drivers
SELECT 
    Request_at AS Day, 
    ROUND(
        SUM(
            CASE 
                WHEN Status = 'completed' THEN 0
                ELSE 1
            END
        ) / COUNT(*), 2) AS 'Cancellation Rate'
FROM (
    SELECT t.* 
    FROM 
    Trips AS t
    LEFT JOIN
    Users AS u
        ON t.Client_Id = u.Users_Id
    LEFT JOIN
    Users AS d
        ON t.Client_Id = d.Users_Id
    WHERE u.Banned = 'No' AND d.Banned = 'No'
        AND Request_at BETWEEN '2013-10-01' AND '2013-10-03'
) AS c
GROUP BY Request_at
ORDER BY 1;