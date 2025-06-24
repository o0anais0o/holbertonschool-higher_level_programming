-- Répertorie tous les enregistrements de second_table où le nom n'est pas vide, classés par score (décroissant)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;

'''
SELECT score, name : Sélectionne uniquement les colonnes score et name dans le résultat.
FROM second_table : Indique que l’on travaille sur la table nommée second_table.
name IS NOT NULL : exclut les lignes où name vaut NULL (valeur inexistante).
name <> '' : exclut les lignes où name est une chaîne vide ('')
ORDER BY score DESC : Trie les résultats par la colonne score dans l’ordre décroissant (du plus grand au plus petit).
'''
