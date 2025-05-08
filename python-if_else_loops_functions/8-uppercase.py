#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    new_str = ""  # Initialise une chaîne vide pour stocker le résultat
    for c in str:  # Parcourt chaque caractère de la chaîne
        # Si le caractère est une minuscule, le convertit en majuscule
        if ord('a') <= ord(c) <= ord('z'):
            new_str += chr(ord(c) - 32)
        else:
            new_str += c  # Sinon, garde le caractère tel quel
    # Affiche la chaîne en majuscules, suivie d’une nouvelle ligne
    print("{}".format(new_str))
