#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Retourne un nouveau dictionnaire avec toutes les valeurs multipliées par 2.
    """
    # Crée un nouveau dictionnaire avec les valeurs multipliées par 2
    new_dict = {}
    for key in a_dictionary:
        # Multiplie la valeur par 2 et l'ajoute au nouveau dictionnaire
        new_dict[key] = a_dictionary[key] * 2
    # Retourne le nouveau dictionnaire
    return new_dict
