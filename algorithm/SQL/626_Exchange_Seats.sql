SELECT (
    CASE
        WHEN MOD(id,2)=1 AND id!=(SELECT COUNT(*) FROM seat) THEN id+1
        WHEN MOD(id,2)=0 THEN id-1
        ELSE id 
    END) AS id
    ,student
FROM seat
ORDER BY id;