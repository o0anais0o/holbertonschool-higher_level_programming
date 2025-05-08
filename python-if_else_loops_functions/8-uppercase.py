#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    # Définit une fonction appelée uppercase qui prend un argument str
    # Docstring : "Affiche une chaîne en majuscules suivie d’un retour à la ligne."

    new_str = ""  
    # Initialise une chaîne vide new_str qui contiendra le résultat final

    for c in str:  
        # Parcourt chaque caractère c de la chaîne str
        if ord('a') <= ord(c) <= ord('z'):
            # Si le caractère c est une lettre minuscule (code ASCII entre 'a' et 'z')
            new_str += chr(ord(c) - 32)
            # Convertit la lettre minuscule en majuscule :
            # - ord(c) donne le code ASCII du caractère c
            # - ord(c) - 32 donne le code ASCII de la lettre majuscule correspondante
            # - chr(...) convertit le code ASCII en caractère
        else:
            new_str += c
            # Si c n’est pas une minuscule, l’ajoute tel quel à new_str

    print("{}".format(new_str))
    # Affiche la chaîne new_str (en majuscules) suivie d’un retour à la ligne
