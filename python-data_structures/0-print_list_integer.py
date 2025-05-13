#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Affiche tous les entiers d'une liste, un par ligne.
    """
    # Parcourt chaque élément de la liste
    for element in my_list:
        # Affiche l'élément sous forme d'entier
        print("{:d}".format(element))
