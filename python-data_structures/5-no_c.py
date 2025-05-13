#!/usr/bin/python3
def no_c(my_string):
    """
    Retourne une nouvelle chaîne sans les caractères 'c' et 'C'.
    """
    # Initialise une chaîne vide pour stocker le résultat
    new_string = ""
    # Parcourt chaque caractère de la chaîne d'origine
    for char in my_string:
        # Ajoute le caractère s'il n'est pas 'c' ou 'C'
        if char != 'c' and char != 'C':
            new_string += char
    # Retourne la nouvelle chaîne sans 'c' ni 'C'
    return new_string
