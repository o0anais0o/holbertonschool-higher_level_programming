#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Retourne un set contenant les éléments présents dans un seul des deux sets.
    """
    # Utilise l'opérateur de différence symétrique pour trouver les éléments uniques
    return set_1 ^ set_2
