#!/usr/bin/python3
"""
Ce module fournit une fonction pour écrire du texte dans un fichier.

Fonction:
    write_file(filename="", text=""):
        Écrit une chaîne de caractères dans un fichier et
        retourne le nombre de caractères écrits.
"""


def write_file(filename="", text=""):
    """
    Écrit une chaîne de caractères dans un fichier texte (créé ou écrasé).

    Args:
        filename (str): Le chemin du fichier où écrire.
        text (str): Le texte à écrire dans le fichier.

    Returns:
        int: Le nombre de caractères écrits dans le fichier.

    Raises:
        Exception: Si l'ouverture ou l'écriture dans le fichier échoue.
    """
    # Ouvre le fichier en mode écriture ("w")
    # Si le fichier existe, il sera écrasé ; sinon, il sera créé
    with open(filename, "w") as f:
        # Écrit le texte dans le fichier et retourne
        # le nombre de caractères écrits
        return f.write(text)
