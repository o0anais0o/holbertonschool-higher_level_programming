#!/usr/bin/python3
"""
Ce module fournit une fonction pour ajouter du texte
à la fin d'un fichier texte.

Fonction :
    append_write(filename="", text=""):
        Ajoute une chaîne de caractères à la fin d'un fichier et
        retourne le nombre de caractères ajoutés.
"""


def append_write(filename="", text=""):
    """
    Ajoute une chaîne de caractères à la fin d'un fichier texte (append mode).

    Si le fichier n'existe pas, il est créé automatiquement.

    Args:
        filename (str): Le chemin du fichier où ajouter le texte.
        text (str): Le texte à ajouter à la fin du fichier.

    Returns:
        int: Le nombre de caractères ajoutés dans le fichier.

    Raises:
        Exception: Si l'ouverture ou l'écriture dans le fichier échoue.
    """
    with open(filename, "a") as f:
        return f.write(text)
