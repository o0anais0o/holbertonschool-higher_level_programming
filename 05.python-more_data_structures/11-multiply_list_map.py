#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Retourne une nouvelle liste avec toutes les valeurs multipliées par number."""
    return list(map(lambda x: x * number, my_list))
