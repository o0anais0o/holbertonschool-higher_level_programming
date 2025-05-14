#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Affiche un dictionnaire en triant les clés par ordre alphabétique.
    """
    # Parcourt les clés triées du dictionnaire
    for key in sorted(a_dictionary):
        # Affiche la clé et sa valeur
        print("{}: {}".format(key, a_dictionary[key]))
