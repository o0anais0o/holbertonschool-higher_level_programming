#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Remplace ou ajoute une paire clé/valeur dans le dictionnaire.
    Si la clé existe, sa valeur est remplacée.
    Si la clé n'existe pas, elle est créée avec la valeur donnée.
    """
    # Ajoute ou met à jour la clé avec la nouvelle valeur
    a_dictionary[key] = value
    # Retourne le dictionnaire mis à jour
    return a_dictionary
