#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Retourne le plus grand entier d'une liste.
    Si la liste est vide, retourne None.
    """
    # Vérifie si la liste est vide
    if len(my_list) == 0:
        return None

    # Initialise le maximum avec le premier élément de la liste
    max_value = my_list[0]

    # Parcourt la liste pour trouver le plus grand entier
    for num in my_list:
        # Met à jour le maximum si un élément plus grand est trouvé
        if num > max_value:
            max_value = num

    # Retourne le plus grand entier trouvé
    return max_value
