#!/usr/bin/python3
def safe_print_integer(value):
    # Tente d'afficher la valeur comme un entier
    try:
        # Affiche la valeur formatée en entier, suivie d'un retour à la ligne
        print("{:d}".format(value))
        # Retourne True si l'affichage a réussi (la valeur est un entier)
        return True
    except (ValueError, KeyError):
        # Si la valeur ne peut pas être formatée en entier, retourne False
        return False
