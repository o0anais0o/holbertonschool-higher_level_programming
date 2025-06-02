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
    with open(filename, "w") as f:
        return f.write(text)
