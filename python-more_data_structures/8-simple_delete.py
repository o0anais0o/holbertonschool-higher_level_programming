#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Supprime une clé d'un dictionnaire si elle existe.
    Si la clé n'existe pas, le dictionnaire ne change pas.
    """
    # Vérifie si la clé existe dans le dictionnaire
    if key in a_dictionary:
        # Supprime la clé du dictionnaire
        del a_dictionary[key]
    # Retourne le dictionnaire (modifié ou non)
    return a_dictionary
