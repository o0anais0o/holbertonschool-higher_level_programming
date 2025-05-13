#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retourne l'élément à l'indice idx d'une liste.
    """
    # Vérifie si l'indice est négatif
    if idx < 0:
        return None

    # Vérifie si l'indice dépasse la taille de la liste
    if idx >= len(my_list):
        return None

    # Retourne l'élément à l'indice demandé
    return my_list[idx]
