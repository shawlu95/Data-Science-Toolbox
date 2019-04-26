SELECT DISTINCT l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l1.Id = l3.Id - 2
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;