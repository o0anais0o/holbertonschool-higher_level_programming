#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Retourne un tuple contenant la longueur de la chaîne et son premier caractère.
    Si la chaîne est vide, le premier caractère est None.
    """
    # Calcule la longueur de la chaîne
    length = len(sentence)

    # Vérifie si la chaîne est vide
    if length == 0:
        # Retourne la longueur et None si la chaîne est vide
        return (0, None)

    # Retourne la longueur et le premier caractère si la chaîne n'est pas vide
    return (length, sentence[0])
