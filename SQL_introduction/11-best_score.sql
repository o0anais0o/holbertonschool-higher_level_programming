-- Répertorie tous les enregistrements avec un score >= 10 de second_table, classés par score (du plus haut au plus bas)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
