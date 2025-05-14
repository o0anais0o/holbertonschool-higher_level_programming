#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Crée une nouvelle liste avec un élément remplacé à l'indice donné.
    """
    # Crée une copie de la liste d'origine
    new_copy = my_list[:]

    # Remplace l'élément à l'indice donné si l'indice est valide
    if 0 <= idx < len(my_list):
        new_copy[idx] = element

    # Retourne la nouvelle liste
    return new_copy
