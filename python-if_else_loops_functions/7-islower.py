#!/usr/bin/python3

def islower(c):
    """Vérifie si un caractère est en minuscule."""
    # Si c est une chaîne vide ou None, retourne False
    if not c:
        return False
    # Compare le code ASCII du caractère avec les codes ASCII de 'a' et 'z'
    # Retourne True si c est une lettre minuscule, False sinon
    return ord('a') <= ord(c) <= ord('z')
