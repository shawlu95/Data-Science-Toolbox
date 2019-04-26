SELECT 
    score, 
    DENSE_RANK() over (ORDER BY score DESC) AS rank
FROM scores;
