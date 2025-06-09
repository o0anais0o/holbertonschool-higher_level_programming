#!/usr/bin/python3
"""
Ce module fournit une fonction pour créer un objet Python
à partir d'un fichier JSON.

Fonction :
    load_from_json_file(filename) :
        Lit un fichier JSON et retourne la structure de données
        Python correspondante.
"""


import json  # Importe le module json pour la désérialisation


def load_from_json_file(filename):
    """
    Crée un objet Python à partir d'un fichier JSON.

    Args:
        filename (str): Le chemin du fichier JSON à lire.

    Returns:
        object: L'objet Python représenté par le contenu JSON du fichier
        (ex : dictionnaire, liste, etc.).
    """
    # Ouvre le fichier en lecture avec le mot-clé 'with' pour garantir
    # sa fermeture automatique
    with open(filename, "r") as f:
        # Lit le contenu du fichier et le convertit en objet Python
        # grâce à json.load
        return json.load(f)
