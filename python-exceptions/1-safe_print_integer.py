#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Try tente d'afficher la valeur comme un entier
        print("{:d}".format(value))
        # Affiche la valeur formatée en entier, suivie d'un retour à la ligne
        return True
        # Retourne True si l'affichage a réussi (la valeur est un entier)
    except (ValueError, KeyError):
        # Si la valeur ne peut pas être formatée en entier, retourne False
        return False
