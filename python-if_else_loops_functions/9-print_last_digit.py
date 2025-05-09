#!/usr/bin/python3

def print_last_digit(number):
    """Affiche et retourne le dernier chiffre d'un nombre."""
    # On prend la valeur absolue pour gérer les nombres négatifs
    last_digit = abs(number) % 10
    # On affiche le dernier chiffre sans retour à la ligne supplémentaire
    print(last_digit, end='')
    # On retourne la valeur du dernier chiffre
    return last_digit
