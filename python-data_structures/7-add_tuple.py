#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Additionne deux tuples et retourne un nouveau tuple de deux entiers.
    Si un tuple a moins de deux éléments, les éléments manquants sont considérés comme 0.
    Si un tuple a plus de deux éléments, seuls les deux premiers sont utilisés.
    """
    # Récupère le premier élément de chaque tuple ou 0 si absent
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0

    # Récupère le deuxième élément de chaque tuple ou 0 si absent
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    # Retourne un tuple contenant la somme des premiers et deuxièmes éléments
    return (a1 + b1, a2 + b2)
