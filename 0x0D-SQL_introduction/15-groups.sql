-- Group rows by score and count
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
