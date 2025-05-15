#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Convertit un nombre romain (sous forme de chaîne) en entier.
    Retourne 0 si l'entrée n'est pas une chaîne ou est None.
    """
    # Vérifie si l'entrée est une chaîne de caractères valide
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Dictionnaire de correspondance des chiffres romains
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_value = 0

    # Parcourt la chaîne de droite à gauche
    for char in reversed(roman_string):
        value = roman_dict.get(char, 0)
        # Si la valeur courante est inférieure à la précédente, on la soustrait
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result
