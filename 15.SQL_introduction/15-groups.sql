-- Liste le nombre d'enregistrements ayant le même score dans la seconde table
-- Résultat : score | nombre (nombre), trié par nombre (décroissant)
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
