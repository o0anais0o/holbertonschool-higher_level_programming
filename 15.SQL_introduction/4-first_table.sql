-- Crée la table first_table si elle n'existe pas
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

'''
id INT :
id : nom de la colonne.
INT : le type de données.
INT signifie entier (integer en anglais), donc cette colonne contiendra
uniquement des nombres entiers (exemple : 1, 42, 1000).
'''
'''
name VARCHAR(256) :
name : le nom de la colonne.
VARCHAR(256) : le type de données.
VARCHAR(256) signifie chaîne de caractères de longueur variable,
avec un maximum de 256 caractères (exemple : "Alice", "Bob", "Charlie").
'''