#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Affiche tous les entiers d'une liste en ordre inverse.
    """
    # Parcourt la liste à l'envers, de la fin vers le début
    for i in range(len(my_list) - 1, -1, -1):
        # Affiche chaque élément sous forme d'entier
        print("{:d}".format(my_list[i]))
