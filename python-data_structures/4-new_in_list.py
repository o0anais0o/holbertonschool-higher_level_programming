#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Crée une nouvelle liste avec un élément remplacé à l'indice donné.
    """
    # Crée une copie de la liste d'origine
    new_copy = my_list[:]

    # Vérifie si l'indice est hors limites
    if idx < 0 or idx >= len(my_list):
        return new_copy

    # Remplace l'élément seulement si l'indice n'est pas 0
    if idx != 0:
        new_copy[idx] = element

    # Retourne la nouvelle liste modifiée ou non
    return new_copy
