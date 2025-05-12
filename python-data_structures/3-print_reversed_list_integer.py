#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Print all integers in a list in reverse order.

    Args:
        my_list (list): The list of integers to print.
    """
    # Itère de la fin de la liste jusqu'au début
    for i in range(len(my_list) - 1, -1, -1):
        # Garantit que les entiers sont affichés sans conversion explicite en chaînes
        print("{:d}".format(my_list[i]))
