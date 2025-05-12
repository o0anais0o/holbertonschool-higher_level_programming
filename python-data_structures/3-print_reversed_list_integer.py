#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Imprimez tous les entiers d'une liste dans l'ordre inverse.

    Args:
    my_list (liste) : La liste des entiers à imprimer.
    """
    # Itère de la fin de la liste jusqu'au début
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
