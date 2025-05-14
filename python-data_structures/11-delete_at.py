#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Supprime l'élément à une position spécifique dans la liste.
    Si l'indice est négatif ou hors limites, la liste reste inchangée.
    """
    # Vérifie si l'indice est valide
    if idx < 0 or idx >= len(my_list):
        # Retourne la liste inchangée si l'indice est invalide
        return my_list

    # Supprime l'élément à l'indice donné
    del my_list[idx]

    # Retourne la liste modifiée
    return my_list
