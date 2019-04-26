-- Write your MySQL query statement below
SELECT 
    f1.follower
    ,COUNT(DISTINCT f2.follower) num
FROM follow f1
JOIN follow f2 
    ON f1.follower = f2.followee
GROUP BY f1.follower

-- for study, f0 does not matter, don't care about original followee
SELECT 
    f1.followee AS 'f0'
    ,f1.follower AS 'f1'
    ,f2.follower AS 'f2'
FROM follow f1
JOIN follow f2 
    ON f1.follower = f2.followee
