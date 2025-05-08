#!/usr/bin/python3

def islower(c):
    # Définit une fonction appelée islower qui prend un caractère 'c' en paramètre

    if ord(c) >= 97 and ord(c) <= 122:
        # ord(c) renvoie le code ASCII du caractère 'c'
        # Les codes ASCII de 97 à 122 correspondent aux lettres minuscules ('a' à 'z')

        return True
        # Si 'c' est une lettre minuscule, la fonction retourne True

    return False
    # Sinon, la fonction retourne False