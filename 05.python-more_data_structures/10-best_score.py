#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Retourne la clé avec la plus grande valeur entière dans le dictionnaire.
    Si le dictionnaire est vide ou None, retourne None.
    """
    # Vérifie si le dictionnaire existe et n'est pas vide
    if not a_dictionary:
        return None

    # Trouve la clé avec la plus grande valeur
    max_key = None
    max_value = float('-inf')
    for key in a_dictionary:
        # Compare chaque valeur à la valeur maximale actuelle
        if a_dictionary[key] > max_value:
            max_value = a_dictionary[key]
            max_key = key

    # Retourne la clé avec la plus grande valeur
    return max_key
