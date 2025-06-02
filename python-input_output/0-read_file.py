#!/usr/bin/python3
"""
Ce module fournit une fonction pour lire et
afficher le contenu d'un fichier texte.

Fonction:
    read_file(filename=""):
        Affiche le contenu d'un fichier texte à l'écran.
"""


def read_file(filename=""):
    """
    Lit un fichier texte et affiche son contenu sur la sortie standard.

    Args:
        filename (str): Le chemin du fichier à lire.

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
        PermissionError:
        Si les permissions sont insuffisantes pour lire le fichier.
        Exception:
        Pour toute autre erreur liée à l'ouverture ou la lecture du fichier.
    """
    with open(filename, "r") as f:
        print(f.read(), end="")
