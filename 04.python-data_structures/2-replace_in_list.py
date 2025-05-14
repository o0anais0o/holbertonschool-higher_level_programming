#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Remplace un élément d'une liste à une position donnée.
    """
    # Vérifie si l'indice est hors limites
    if idx < 0 or idx >= len(my_list):
        return my_list
    # Remplace l'élément à l'indice donné par le nouvel élément
    my_list[idx] = element
    # Retourne la liste modifiée
    return my_list
