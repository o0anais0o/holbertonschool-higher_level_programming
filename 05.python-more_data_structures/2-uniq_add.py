#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Additionne tous les entiers uniques d'une liste.
    Chaque entier n'est compté qu'une seule fois.
    """
    # Utilise un set pour obtenir les éléments uniques de la liste
    unique_elements = set(my_list)

    # Calcule la somme des éléments uniques
    total = 0
    for num in unique_elements:
        total += num

    # Retourne le résultat
    return total
